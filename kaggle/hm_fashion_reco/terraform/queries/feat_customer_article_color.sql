WITH stats AS (
  SELECT
    dates.obs_dat,
    customer_short_id,
    COUNT(*) AS num_purchases
    FROM `zenscr-seefood-dev.hm_kaggle_reco.feat_base_dates` dates
    LEFT JOIN `zenscr-seefood-dev.hm_kaggle_reco.sample_transactions` AS trans
          ON dates.t_dat = trans.t_dat
  GROUP BY dates.obs_dat, customer_short_id
)
SELECT
  dates.obs_dat,
  trans.customer_short_id,
  colour_group_code AS feat_colour_group_code,
  COUNT(*) / ANY_VALUE(num_purchases) AS feat_colour_group_code_affinity,
  COUNT(*) feat_num_colour_group_code_events
FROM `zenscr-seefood-dev.hm_kaggle_reco.feat_base_dates` dates
LEFT JOIN `zenscr-seefood-dev.hm_kaggle_reco.sample_transactions` AS trans
       ON dates.t_dat = trans.t_dat
LEFT JOIN `zenscr-seefood-dev.hm_kaggle.articles` AS articles
       ON trans.article_id = articles.article_id
LEFT JOIN `zenscr-seefood-dev.hm_kaggle.customers` AS customers
       ON trans.customer_short_id = customers.customer_short_id
LEFT JOIN stats
       ON dates.obs_dat = stats.obs_dat AND trans.customer_short_id = stats.customer_short_id
GROUP BY obs_dat, customer_short_id, colour_group_code

