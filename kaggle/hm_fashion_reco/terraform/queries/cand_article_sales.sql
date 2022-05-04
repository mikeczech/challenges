WITH customers AS (
  SELECT
    DISTINCT
    obs_dat,
    customer_id
  FROM `zenscr-seefood-dev.hm_kaggle_reco.ground_truth`
),
popular_articles AS (
  SELECT
      obs_dat,
      article_id,
      num_sales,
      0 AS relevance
  FROM `zenscr-seefood-dev.hm_kaggle_reco.misc_article_sales`
  WHERE sales_rank <= 390
)
SELECT
  c.obs_dat,
  customer_id,
  article_id,
  num_sales AS score,
  relevance
FROM customers c
CROSS JOIN popular_articles
