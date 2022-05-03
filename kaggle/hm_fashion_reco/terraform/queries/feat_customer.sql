SELECT
  dates.obs_dat,
  customer_id,
  AVG(price) AS feat_price_affinity,
  COUNTIF(perceived_colour_value_name = "Dark") / COUNT(*) AS feat_dark_affinity,
  COUNTIF(perceived_colour_value_name = "Dusty Light") / COUNT(*) AS feat_dusty_light_affinity,
  COUNT(*) AS feat_num_sales
FROM `zenscr-seefood-dev.hm_kaggle_reco.feat_base_dates` dates
LEFT JOIN `zenscr-seefood-dev.hm_kaggle.transactions` AS trans
       ON dates.t_dat = trans.t_dat
LEFT JOIN `zenscr-seefood-dev.hm_kaggle.articles` AS articles
       ON trans.article_id = articles.article_id
GROUP BY obs_dat, customer_id 
