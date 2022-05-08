WITH dates AS (
  SELECT
    obs_dat
  FROM
    UNNEST(GENERATE_DATE_ARRAY("2020-04-01", "2020-09-23", INTERVAL 7 DAY)) AS obs_dat
),
sales AS (
  SELECT
    obs_dat,
    trans.article_id,
    COUNT(*) AS num_sales,
    SUM(price) AS revenue
  FROM dates
  LEFT JOIN `zenscr-seefood-dev.hm_kaggle_reco.sample_transactions` trans
         ON trans.t_dat < obs_dat AND trans.t_dat >= DATE_SUB(obs_dat, INTERVAL 14 DAY)
  LEFT JOIN `zenscr-seefood-dev.hm_kaggle.articles` articles
         ON trans.article_id = articles.article_id
  GROUP BY obs_dat, article_id
)
SELECT
  obs_dat,
  article_id,
  num_sales,
  revenue,
  DENSE_RANK() OVER (PARTITION BY obs_dat ORDER BY num_sales DESC) AS sales_rank,
  DENSE_RANK() OVER (PARTITION BY obs_dat ORDER BY revenue DESC) AS revenue_rank
FROM sales
