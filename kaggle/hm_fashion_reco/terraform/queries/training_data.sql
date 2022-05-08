WITH gt_and_cand AS (
  SELECT
    obs_dat,
    customer_short_id,
    article_id,
    -1.0 AS article_similarity_score,
    -1.0 AS article_sales_score,
    -1.0 AS prev_purchases_score,
    -1.0 AS article_department_sales_score,
    relevance
  FROM `zenscr-seefood-dev.hm_kaggle_reco.ground_truth`
  UNION ALL
  SELECT
    obs_dat,
    customer_short_id,
    article_id,
    score AS article_similarity_score,
    num_sales AS article_sales_score,
    -1.0 AS prev_purchases_score,
    -1.0 AS article_department_sales_score,
    sim.relevance
  FROM `zenscr-seefood-dev.hm_kaggle_reco.cand_article_similarity` sim
  INNER JOIN `zenscr-seefood-dev.hm_kaggle_reco.cand_article_sales`
  USING (obs_dat, customer_short_id, article_id)
  UNION ALL
  SELECT
    obs_dat,
    customer_short_id,
    article_id,
    -1.0 AS article_similarity_score,
    num_sales AS article_sales_score,
    -1.0 AS prev_purchases_score,
    -1.0 AS article_department_sales_score,
    relevance
  FROM `zenscr-seefood-dev.hm_kaggle_reco.cand_article_sales`
  UNION ALL
  SELECT
    obs_dat,
    customer_short_id,
    article_id,
    -1.0 AS article_similarity_score,
    -1.0 AS article_sales_score,
    num_purchases AS prev_purchases_score,
    -1.0 AS article_department_sales_score,
    relevance
  FROM `zenscr-seefood-dev.hm_kaggle_reco.cand_prev_purchases`
),
base AS (
  SELECT
      obs_dat,
      customer_short_id,
      article_id,
      MAX(article_similarity_score) AS article_similarity_score,
      MAX(article_sales_score) AS article_sales_score,
      MAX(prev_purchases_score) AS prev_purchases_score,
      MAX(article_department_sales_score) AS article_department_sales_score,
      MAX(relevance) AS relevance
  FROM gt_and_cand
  GROUP BY obs_dat, customer_short_id, article_id
)
SELECT
  base.obs_dat,
  base.customer_short_id,
  base.article_id,

  -- target
  base.relevance,

  -- candidate selection scores
  article_similarity_score,
  article_sales_score,
  prev_purchases_score,
  article_department_sales_score,

  -- customer features
  feat_customer_age,
  feat_customer_price_affinity,
  feat_customer_stdev_price,
  feat_customer_num_purchases

  -- article features
  feat_article_average_price,
  feat_article_stdev_price,
  feat_article_num_sales,
  feat_article_num_distinct_customers,
  feat_article_average_age,
  feat_article_stdev_age,

  feat_article_colour_group_code,
  feat_article_perceived_colour_value_id,
  feat_article_section_no,
  feat_article_index_code,
  feat_article_garment_group_no
FROM base
LEFT JOIN hm_kaggle_reco.feat_customer fc
       ON base.obs_dat = fc.obs_dat AND base.customer_short_id = fc.customer_short_id
LEFT JOIN hm_kaggle_reco.feat_article fa
       ON base.obs_dat = fa.obs_dat AND base.article_id = fa.article_id
