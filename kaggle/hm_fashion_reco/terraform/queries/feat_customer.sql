SELECT
  dates.obs_dat,
  trans.customer_short_id,
  ANY_VALUE(COALESCE(age, 0.0)) AS feat_customer_age,
  AVG(COALESCE(price, 0.0)) AS feat_customer_price_affinity,
  STDDEV(COALESCE(price, 0.0)) AS feat_customer_stdev_price,
  COUNT(*) AS feat_customer_num_purchases,
  DATE_DIFF(obs_dat, MAX(dates.t_dat), DAY) feat_customer_last_purchase_num_days,
  CASE
    WHEN ANY_VALUE(club_member_status) = "ACTIVE" THEN 0
    WHEN ANY_VALUE(club_member_status) = "PRE-CREATE" THEN 1
    WHEN ANY_VALUE(club_member_status) = "LEFT CLUB" THEN 2
    ELSE NULL
  END AS feat_customer_club_member_status,
  ANY_VALUE(FN) AS feat_customer_fn,
  ANY_VALUE(Active) AS feat_customer_active,
  CASE
    WHEN ANY_VALUE(fashion_news_frequency) = "Regularly" THEN 0
    WHEN ANY_VALUE(fashion_news_frequency) = "Monthly" THEN 1
    WHEN ANY_VALUE(fashion_news_frequency) = "NONE"  THEN 2
    ELSE NULL
  END AS feat_customer_fashion_news_frequency,
  COUNTIF(sales_channel_id = 1) / COUNT(*) AS feat_customer_sales_channel_one_affinity,
  COUNTIF(sales_channel_id = 2) / COUNT(*) AS feat_customer_sales_channel_two_affinity
FROM `zenscr-seefood-dev.hm_kaggle_reco.feat_base_dates` dates
LEFT JOIN `zenscr-seefood-dev.hm_kaggle_reco.sample_transactions` AS trans
       ON dates.t_dat = trans.t_dat
LEFT JOIN `zenscr-seefood-dev.hm_kaggle.articles` AS articles
       ON trans.article_id = articles.article_id
LEFT JOIN `zenscr-seefood-dev.hm_kaggle.customers` AS customers
       ON trans.customer_short_id = customers.customer_short_id
GROUP BY obs_dat, customer_short_id

