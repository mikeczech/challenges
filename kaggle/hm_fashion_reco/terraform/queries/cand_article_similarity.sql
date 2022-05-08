WITH base AS (
  SELECT
    DISTINCT
    dates.obs_dat,
    trans.customer_short_id,
    CAST(trans.article_id AS STRING) AS article_id,
    DENSE_RANK() OVER (PARTITION BY dates.obs_dat, trans.customer_short_id ORDER BY dates.t_dat DESC) AS rank
  FROM `zenscr-seefood-dev.hm_kaggle_reco.feat_base_dates` dates
  LEFT JOIN `zenscr-seefood-dev.hm_kaggle_reco.sample_transactions` AS trans
        ON dates.t_dat = trans.t_dat AND trans.t_dat >= DATE_SUB(obs_dat, INTERVAL 365 DAY)
  QUALIFY rank <= 100
)

SELECT
  base.obs_dat,
  base.customer_short_id,
  CAST(similar_article_id AS INT64) AS article_id,
  ROW_NUMBER() OVER (
    PARTITION BY
      base.obs_dat,
      base.customer_short_id,
      base.article_id
    ORDER BY score DESC
  ) AS rank,
  score,
  0 AS relevance
FROM base
LEFT JOIN `zenscr-seefood-dev.hm_kaggle_reco.misc_similar_articles` AS sim
      ON base.article_id = sim.article_id
QUALIFY rank <= 500
