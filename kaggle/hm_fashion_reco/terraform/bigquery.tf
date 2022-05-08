resource "google_bigquery_dataset" "hm_kaggle_reco" {
  dataset_id                  = "hm_kaggle_reco"
  friendly_name               = "H&M Recommendation Data"
  description                 = "Data for recommending H&M products"
  location                    = "us-central1"
}

resource "google_bigquery_table" "customers_sample_001" {
  dataset_id = google_bigquery_dataset.hm_kaggle_reco.dataset_id
  table_id   = "sample_customers_001"
  view {
    query = file("queries/sampling/customers_001.sql")
    use_legacy_sql = false
  }
}

resource "google_bigquery_table" "customers_sample_01" {
  dataset_id = google_bigquery_dataset.hm_kaggle_reco.dataset_id
  table_id   = "sample_customers_01"
  view {
    query = file("queries/sampling/customers_01.sql")
    use_legacy_sql = false
  }
}

resource "google_bigquery_table" "customers_sample_05" {
  dataset_id = google_bigquery_dataset.hm_kaggle_reco.dataset_id
  table_id   = "sample_customers_05"
  view {
    query = file("queries/sampling/customers_05.sql")
    use_legacy_sql = false
  }
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

resource "google_bigquery_table" "feature_article" {
  dataset_id = google_bigquery_dataset.hm_kaggle_reco.dataset_id
  table_id   = "feat_article"
  view {
    query = file("queries/feat_article.sql")
    use_legacy_sql = false
  }
}

resource "google_bigquery_table" "feature_customer_article_color" {
  dataset_id = google_bigquery_dataset.hm_kaggle_reco.dataset_id
  table_id   = "feat_customer_article_color"
  view {
    query = file("queries/feat_customer_article_color.sql")
    use_legacy_sql = false
  }
}

resource "google_bigquery_table" "cand_article_sales" {
  dataset_id = google_bigquery_dataset.hm_kaggle_reco.dataset_id
  table_id   = "cand_article_sales"
  view {
    query = file("queries/cand_article_sales.sql")
    use_legacy_sql = false
  }
}

resource "google_bigquery_table" "cand_article_similarity" {
  dataset_id = google_bigquery_dataset.hm_kaggle_reco.dataset_id
  table_id   = "cand_article_similarity"
  view {
    query = file("queries/cand_article_similarity.sql")
    use_legacy_sql = false
  }
}

resource "google_bigquery_table" "cand_prev_purchases" {
  dataset_id = google_bigquery_dataset.hm_kaggle_reco.dataset_id
  table_id   = "cand_prev_purchases"
  view {
    query = file("queries/cand_prev_purchases.sql")
    use_legacy_sql = false
  }
}

resource "google_bigquery_table" "cand_article_department_sales" {
  dataset_id = google_bigquery_dataset.hm_kaggle_reco.dataset_id
  table_id   = "cand_article_department_sales"
  view {
    query = file("queries/cand_article_department_sales.sql")
    use_legacy_sql = false
  }
}

resource "google_bigquery_table" "training_data" {
  dataset_id = google_bigquery_dataset.hm_kaggle_reco.dataset_id
  table_id   = "training_data"
  view {
    query = file("queries/training_data.sql")
    use_legacy_sql = false
  }
}
