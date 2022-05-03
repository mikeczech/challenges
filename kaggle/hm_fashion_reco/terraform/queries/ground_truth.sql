WITH dates AS (
  SELECT
    obs_dat,
    t_dat
  FROM
    UNNEST(GENERATE_DATE_ARRAY("2020-04-01", "2020-09-23")) AS obs_dat
  LEFT JOIN
    UNNEST(GENERATE_DATE_ARRAY(obs_dat, "2020-09-23")) AS t_dat
  ON
    t_dat <= DATE_ADD(obs_dat, INTERVAL 6 DAY)
)
SELECT
  dates.obs_dat,
  dates.t_dat,
  customer_id,
  article_id,
  1 AS relevance
FROM dates
LEFT JOIN `zenscr-seefood-dev.hm_kaggle.transactions` AS trans
       ON dates.t_dat = trans.t_dat
