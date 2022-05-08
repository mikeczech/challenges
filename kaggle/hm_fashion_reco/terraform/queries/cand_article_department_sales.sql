WITH dates AS (
  SELECT
    obs_dat
  FROM
    UNNEST(GENERATE_DATE_ARRAY("2020-04-01", "2020-09-23", INTERVAL 7 DAY)) AS obs_dat
),
customers AS (
  SELECT
    DISTINCT
    customer_short_id,
    department_no
  FROM dates
  LEFT JOIN `zenscr-seefood-dev.hm_kaggle_reco.sample_transactions` trans
         ON trans.t_dat < obs_dat
  LEFT JOIN `zenscr-seefood-dev.hm_kaggle.articles` articles
         ON trans.article_id = articles.article_id
  WHERE t_dat < obs_dat
),
department_sales AS (
  SELECT
    obs_dat,
    department_no,
    trans.article_id,
    COUNT(*) AS num_sales,
    SUM(price) AS revenue
  FROM dates
  LEFT JOIN `zenscr-seefood-dev.hm_kaggle_reco.sample_transactions` trans
         ON trans.t_dat < obs_dat AND trans.t_dat >= DATE_SUB(obs_dat, INTERVAL 64 DAY)
  LEFT JOIN `zenscr-seefood-dev.hm_kaggle.articles` articles
         ON trans.article_id = articles.article_id
  GROUP BY obs_dat, department_no, article_id
),
ranked_sales AS (
  SELECT
    obs_dat,
    department_no,
    article_id,
    num_sales,
    ROW_NUMBER() OVER (PARTITION BY obs_dat, department_no ORDER BY num_sales DESC, revenue DESC) AS sales_rank,
  FROM department_sales
  QUALIFY sales_rank <= 50
)
SELECT
  dates.obs_dat,
  customers.customer_short_id,
  customers.department_no,
  article_id,
  num_sales,
  0 AS relevance
FROM dates
CROSS JOIN customers
FULL OUTER JOIN ranked_sales r
             ON  dates.obs_dat = r.obs_dat AND customers.department_no = r.department_no
