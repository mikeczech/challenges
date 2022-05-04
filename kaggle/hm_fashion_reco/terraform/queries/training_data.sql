WITH gt_and_neg AS (
  SELECT 
    obs_dat,
    customer_id,
    article_id,
    -1.0 AS score,
    relevance
  FROM `zenscr-seefood-dev.hm_kaggle_reco.ground_truth`
  UNION ALL
  SELECT
    obs_dat,
    customer_id,
    article_id,
    score,
    relevance
  FROM `zenscr-seefood-dev.hm_kaggle_reco.cand_article_sales`
)
SELECT
    obs_dat,
    customer_id,
    article_id,
    MAX(score) AS score,
    MAX(relevance) AS relevance
FROM gt_and_neg
GROUP BY obs_dat, customer_id, article_id
