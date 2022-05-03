WITH dates AS (
  SELECT
    obs_dat
  FROM
    UNNEST(GENERATE_DATE_ARRAY("2020-04-01", "2020-09-23")) AS obs_dat
),
sales AS (
  SELECT
    obs_dat,
    section_no,
    articles.product_code,
    trans.article_id,
    COUNT(*) num_sales
  FROM dates
  LEFT JOIN `zenscr-seefood-dev.hm_kaggle.transactions` trans
         ON trans.t_dat < obs_dat AND trans.t_dat >= DATE_SUB(obs_dat, INTERVAL 7 DAY)
  LEFT JOIN `zenscr-seefood-dev.hm_kaggle.articles` articles
         ON trans.article_id = articles.article_id
  GROUP BY obs_dat, section_no, articles.product_code, article_id
)
SELECT
  obs_dat,
  section_no,
  product_code,
  article_id,
  num_sales,
  DENSE_RANK() OVER (PARTITION BY obs_dat, section_no ORDER BY num_sales DESC) AS rank
FROM sales
