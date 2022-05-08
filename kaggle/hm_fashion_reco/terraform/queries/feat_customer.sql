SELECT
  dates.obs_dat,
  trans.customer_short_id,
  ANY_VALUE(COALESCE(age, 0.0)) AS feat_customer_age,
  AVG(COALESCE(price, 0.0)) AS feat_customer_price_affinity,
  STDDEV(COALESCE(price, 0.0)) AS feat_customer_stdev_price,
  COUNT(*) AS feat_customer_num_purchases
FROM `zenscr-seefood-dev.hm_kaggle_reco.feat_base_dates` dates
LEFT JOIN `zenscr-seefood-dev.hm_kaggle_reco.sample_transactions` AS trans
       ON dates.t_dat = trans.t_dat
LEFT JOIN `zenscr-seefood-dev.hm_kaggle.articles` AS articles
       ON trans.article_id = articles.article_id
LEFT JOIN `zenscr-seefood-dev.hm_kaggle.customers` AS customers
       ON trans.customer_short_id = customers.customer_short_id
GROUP BY obs_dat, customer_short_id
