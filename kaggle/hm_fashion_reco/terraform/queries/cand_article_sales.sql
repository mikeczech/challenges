WITH dates AS (
  SELECT
    obs_dat
  FROM
    UNNEST(GENERATE_DATE_ARRAY("2020-04-01", "2020-09-23", INTERVAL 7 DAY)) AS obs_dat
),
customers AS (
  SELECT customer_short_id FROM `zenscr-seefood-dev.hm_kaggle_reco.sample_customers_01`
),
sales AS (
  SELECT
    obs_dat,
    trans.article_id,
    COUNT(*) AS num_sales,
    SUM(price) AS revenue
  FROM dates
  LEFT JOIN `zenscr-seefood-dev.hm_kaggle_reco.sample_transactions` trans
         ON trans.t_dat < obs_dat AND trans.t_dat >= DATE_SUB(obs_dat, INTERVAL 28 DAY)
  LEFT JOIN `zenscr-seefood-dev.hm_kaggle.articles` articles
         ON trans.article_id = articles.article_id
  GROUP BY obs_dat, article_id
),
ranked_sales AS (
  SELECT
    obs_dat,
    article_id,
    num_sales,
    ROW_NUMBER() OVER (PARTITION BY obs_dat ORDER BY num_sales DESC, revenue DESC) AS sales_rank,
  FROM sales
  QUALIFY sales_rank <= 2000
)
SELECT
  dates.obs_dat,
  customers.customer_short_id,
  article_id,
  num_sales,
  0 AS relevance
FROM dates
CROSS JOIN customers
FULL OUTER JOIN ranked_sales r
             ON  dates.obs_dat = r.obs_dat
