SELECT
  dates.obs_dat,
  trans.article_id,
  AVG(price) AS feat_average_price,
  STDDEV(price) AS feat_stdev_price,
  COUNT(*) AS feat_num_sales,
  COUNT(DISTINCT trans.customer_id) AS feat_num_distinct_customers,
  AVG(age) AS feat_average_age,
  STDDEV(age) AS feat_stdev_age,

  COUNTIF(EXTRACT(QUARTER FROM dates.t_dat) = 1) / COUNT(*) feat_q1_popularity,
  COUNTIF(EXTRACT(QUARTER FROM dates.t_dat) = 2) / COUNT(*) feat_q2_popularity,
  COUNTIF(EXTRACT(QUARTER FROM dates.t_dat) = 3) / COUNT(*) feat_q3_popularity,
  COUNTIF(EXTRACT(QUARTER FROM dates.t_dat) = 4) / COUNT(*) feat_q4_popularity,

  -- categorical
  ANY_VALUE(product_type_no) AS feat_product_type_no,
  ANY_VALUE(graphical_appearance_no) AS feat_graphical_appearance_no,
  ANY_VALUE(colour_group_code) AS feat_colour_group_code,
  ANY_VALUE(perceived_colour_value_id) AS feat_perceived_colour_value_id,
  ANY_VALUE(perceived_colour_master_id) AS feat_perceived_colour_master_id,
  ANY_VALUE(department_no) AS feat_department_no, -- high cardinality
  ANY_VALUE(index_code) AS feat_index_code,
  ANY_VALUE(section_no) AS feat_section_no,
  ANY_VALUE(garment_group_no) AS feat_garment_group_no

FROM `zenscr-seefood-dev.hm_kaggle_reco.feat_base_dates` dates
LEFT JOIN `zenscr-seefood-dev.hm_kaggle.transactions` AS trans
       ON dates.t_dat = trans.t_dat
LEFT JOIN `zenscr-seefood-dev.hm_kaggle.articles` AS articles
       ON trans.article_id = articles.article_id
LEFT JOIN `zenscr-seefood-dev.hm_kaggle.customers` AS customers
       ON trans.customer_id = customers.customer_id
GROUP BY obs_dat, article_id
