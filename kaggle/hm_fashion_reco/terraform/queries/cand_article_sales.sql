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
      sales_rank,
      0 AS relevance
  FROM `zenscr-seefood-dev.hm_kaggle_reco.misc_article_sales`
  WHERE sales_rank <= 600
)
SELECT
  c.obs_dat,
  customer_id,
  article_id,
  sales_rank,
  num_sales AS score,
  relevance
FROM customers c
FULL OUTER JOIN popular_articles p
            ON c.obs_dat = p.obs_dat
