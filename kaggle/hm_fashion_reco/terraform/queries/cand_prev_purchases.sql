WITH dates AS (
  SELECT
    obs_dat
  FROM
    UNNEST(GENERATE_DATE_ARRAY("2020-04-01", "2020-09-23", INTERVAL 7 DAY)) AS obs_dat
)
SELECT
  obs_dat,
  trans.customer_short_id,
  trans.article_id,
  COUNT(*) AS num_purchases,
  0 AS relevance
FROM dates
LEFT JOIN `zenscr-seefood-dev.hm_kaggle_reco.sample_transactions` trans
        ON trans.t_dat < obs_dat
GROUP BY obs_dat, trans.customer_short_id, trans.article_id
