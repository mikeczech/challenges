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
