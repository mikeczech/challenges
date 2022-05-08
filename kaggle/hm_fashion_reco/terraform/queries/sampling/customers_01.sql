SELECT
  customer_short_id
FROM `zenscr-seefood-dev.hm_kaggle.customers`
WHERE ABS(MOD(FARM_FINGERPRINT(CAST(customer_short_id AS STRING)), 100)) <= 1
