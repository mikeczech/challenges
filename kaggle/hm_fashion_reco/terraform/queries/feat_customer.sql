SELECT
  dates.obs_dat,
  trans.customer_id,
  ANY_VALUE(age) AS feat_age,
  AVG(price) AS feat_price_affinity,
  STDDEV(price) AS feat_stdev_price,  
  COUNT(*) AS feat_num_purchases
FROM `zenscr-seefood-dev.hm_kaggle_reco.feat_base_dates` dates
LEFT JOIN `zenscr-seefood-dev.hm_kaggle.transactions` AS trans
       ON dates.t_dat = trans.t_dat
LEFT JOIN `zenscr-seefood-dev.hm_kaggle.articles` AS articles
       ON trans.article_id = articles.article_id
LEFT JOIN `zenscr-seefood-dev.hm_kaggle.customers` AS customers
       ON trans.customer_id = customers.customer_id
GROUP BY obs_dat, customer_id 
