import argparse
import os
from typing import List
from joblib import dump, load

from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import FunctionTransformer, OrdinalEncoder
from sklearn.compose import ColumnTransformer

import lightgbm
import pandas as pd

FEATURES = [
    "score",
    "feat_price_affinity",
    "feat_dark_affinity",
    "feat_dusty_light_affinity"
]


def select_columns(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    """
    Selects columns and returns a dataframe with only those.

    Usually used with a FunctionTransformer.
    """
    return df[cols]


def to_dataframe(X, col_labels: List[str]):
    """
    Creates a dataframe from an array and associates a label with each column.

    This is mainly needed for scikit-learn's unfortunate support for pandas.
    """
    return pd.DataFrame(X, columns=col_labels)


def get_pipeline(features: List[str]):
    return Pipeline(
        [
            (
                "to_dataframe",
                FunctionTransformer(
                    to_dataframe,
                    kw_args={"col_labels": features},
                ),
            ),
        ]
    )


def get_ranker_pipeline(
    features=FEATURES,
):
    """
    A pipeline based on LightGBM.
    """
    return Pipeline(
        [
            ("features", get_pipeline(features)),
            (
                "ranker",
                lightgbm.LGBMRanker(
                    objective="lambdarank",
                    metric="ndcg",
                )
            ),
        ]
    )

