WITH gt_and_neg AS (
  SELECT 
    obs_dat,
    customer_id,
    article_id,
    -1 AS rank,
    relevance
  FROM `zenscr-seefood-dev.hm_kaggle_reco.ground_truth`
  UNION ALL
  SELECT
    obs_dat,
    customer_id,
    article_id,
    rank,
    relevance
  FROM `zenscr-seefood-dev.hm_kaggle_reco.neg_by_popularity` WHERE rank <= 100
)
SELECT
    obs_dat,
    customer_id,
    article_id,
    MAX(rank) AS rank,
    MAX(relevance) AS relevance
FROM gt_and_neg
WHERE obs_dat = "2020-04-01"
GROUP BY obs_dat, customer_id, article_id
