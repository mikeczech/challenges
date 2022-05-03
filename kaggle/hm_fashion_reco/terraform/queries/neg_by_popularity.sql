WITH visited_sections AS (
  SELECT
    DISTINCT
    gt.obs_dat,
    customer_id,
    gt.section_no
  FROM `zenscr-seefood-dev.hm_kaggle_reco.ground_truth` gt
)
SELECT 
    v.obs_dat,
    v.customer_id,
    v.section_no,
    s.article_id,
    num_sales,
    s.rank,
    0 AS relevance
FROM visited_sections v
LEFT JOIN `zenscr-seefood-dev.hm_kaggle_reco.misc_article_sales` s
       ON v.obs_dat = s.obs_dat AND v.section_no = s.section_no
