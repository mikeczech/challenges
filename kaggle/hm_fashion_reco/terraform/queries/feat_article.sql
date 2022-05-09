WITH base AS (
  SELECT
    dates.obs_dat,
    dates.t_dat,
    trans.article_id,
    price,
    age
  FROM `zenscr-seefood-dev.hm_kaggle_reco.feat_base_dates` dates
  LEFT JOIN `zenscr-seefood-dev.hm_kaggle.transactions` AS trans
         ON dates.t_dat = trans.t_dat
  LEFT JOIN `zenscr-seefood-dev.hm_kaggle.customers` AS customers
         ON trans.customer_short_id = customers.customer_short_id
),
window_feat_1day AS (
  SELECT
    obs_dat,
    article_id,
    COUNT(*) AS feat_article_num_sales_1day,
    AVG(price) AS feat_article_avg_price_1day
  FROM base
  WHERE t_dat = DATE_SUB(obs_dat, INTERVAL 1 DAY)
  GROUP BY obs_dat, article_id
),
window_feat_3day AS (
  SELECT
    obs_dat,
    article_id,
    COUNT(*) AS feat_article_num_sales_3day,
    AVG(price) AS feat_article_avg_price_3day
  FROM base
  WHERE t_dat >= DATE_SUB(obs_dat, INTERVAL 4 DAY)
  GROUP BY obs_dat, article_id
),
window_feat_7day AS (
  SELECT
    obs_dat,
    article_id,
     COUNT(*) AS feat_article_num_sales_7day,
    AVG(price) AS feat_article_avg_price_7day
  FROM base
  WHERE t_dat >= DATE_SUB(obs_dat, INTERVAL 8 DAY)
  GROUP BY obs_dat, article_id
),
features AS (
  SELECT
    base.obs_dat,
    base.article_id,
    AVG(age) AS feat_article_avg_customer_age,
    ANY_VALUE(product_type_no) AS feat_article_product_type_no,
    ANY_VALUE(graphical_appearance_no) AS feat_article_graphical_appearance_no,
    ANY_VALUE(colour_group_code) AS feat_article_colour_group_code,
    ANY_VALUE(perceived_colour_value_id) AS feat_article_perceived_colour_value_id,
    ANY_VALUE(perceived_colour_master_id) AS feat_article_perceived_colour_master_id,
    ANY_VALUE(department_no) AS article_department_no, -- high cardinality
    ANY_VALUE(index_code) AS feat_article_index_code,
    ANY_VALUE(section_no) AS feat_article_section_no,
    ANY_VALUE(garment_group_no) AS feat_article_garment_group_no
  FROM base
  LEFT JOIN `zenscr-seefood-dev.hm_kaggle.articles` AS articles
        ON base.article_id = articles.article_id
  GROUP BY obs_dat, article_id
)
SELECT * FROM features
LEFT JOIN window_feat_1day
USING (obs_dat, article_id)
LEFT JOIN window_feat_3day
USING (obs_dat, article_id)
LEFT JOIN window_feat_7day
USING (obs_dat, article_id)
