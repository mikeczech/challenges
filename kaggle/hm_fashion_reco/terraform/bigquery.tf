resource "google_bigquery_dataset" "hm_kaggle_reco" {
  dataset_id                  = "hm_kaggle_reco"
  friendly_name               = "H&M Recommendation Data"
  description                 = "Data for recommending H&M products"
  location                    = "us-central1"
}

resource "google_bigquery_table" "ground_truth" {
  dataset_id = google_bigquery_dataset.hm_kaggle_reco.dataset_id
  table_id   = "ground_truth"
  view {
    query = file("queries/ground_truth.sql")
    use_legacy_sql = false
  }
}

resource "google_bigquery_table" "feature_base_dates" {
  dataset_id = google_bigquery_dataset.hm_kaggle_reco.dataset_id
  table_id   = "feat_base_dates"
  view {
    query = file("queries/feat_base_dates.sql")
    use_legacy_sql = false
  }
}

resource "google_bigquery_table" "feature_customer" {
  dataset_id = google_bigquery_dataset.hm_kaggle_reco.dataset_id
  table_id   = "feat_customer"
  view {
    query = file("queries/feat_customer.sql")
    use_legacy_sql = false
  }
}

resource "google_bigquery_table" "misc_article_sales" {
  dataset_id = google_bigquery_dataset.hm_kaggle_reco.dataset_id
  table_id   = "misc_article_sales"
  view {
    query = file("queries/misc_article_sales.sql")
    use_legacy_sql = false
  }
}
