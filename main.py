import os
import pandas as pd
from config import (
    PROJECT_ID,
    BUCKET_NAME,
    DATASET_ID,
    RAW_TABLE_ID,
    PROCESSED_TABLE_ID,
)
from utils import (
    upload_to_gcs,
    create_bq_table_from_gcs,
    write_to_bq,
)
from transformations import clean_and_transform_data
from google.cloud import storage
from google.cloud import bigquery
import io

def read_gcs_file(bucket_name, file_path):
    """Read a CSV file from GCS into a Pandas DataFrame."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_path)
    data = blob.download_as_string()
    return pd.read_csv(io.StringIO(data.decode("utf-8")))

def analyze_data():

    client = bigquery.Client(project=PROJECT_ID)
    query = f"""
        SELECT
            Category,
            ROUND(AVG(SalesPerQuantity), 2) AS AvgSalesPerQuantity,
            COUNT(*) AS OrderCount
        FROM `{PROJECT_ID}.{DATASET_ID}.{PROCESSED_TABLE_ID}`
        GROUP BY Category
        ORDER BY AvgSalesPerQuantity DESC
    """
    results = client.query(query).result()
    df = pd.DataFrame([dict(row) for row in results])
    return df

def main():
    # Step 1: Upload file to GCS
    local_file = "hash_sales_data.csv"
    gcs_file_path = "raw_data/sales_data.csv"
    upload_to_gcs(BUCKET_NAME, local_file, gcs_file_path)

    # Step 2: Create BigQuery table from GCS file schema
    gcs_uri = f"gs://{BUCKET_NAME}/{gcs_file_path}"
    create_bq_table_from_gcs(PROJECT_ID, DATASET_ID, RAW_TABLE_ID, gcs_uri)

    # Step 3: Read data from BigQuery, transform, and write back
    raw_df = read_gcs_file(BUCKET_NAME, gcs_file_path)
    transformed_df = clean_and_transform_data(raw_df)
    write_to_bq(PROJECT_ID, DATASET_ID, PROCESSED_TABLE_ID, transformed_df)

    # Step 4: Perform analysis and save results
    analysis_df = analyze_data()


if __name__ == "__main__":
    main()
