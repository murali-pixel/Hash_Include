from google.cloud import storage, bigquery
import os

def upload_to_gcs(bucket_name, local_file, gcs_file_path):
    from google.cloud import storage

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(gcs_file_path)

    
    source_file_name = os.path.abspath(local_file)

   
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {gcs_file_path}.")

def create_bq_table_from_gcs(project_id, dataset_id, table_id, gcs_uri):
    """Create a BigQuery table based on a CSV file schema."""
    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        autodetect=True,
        skip_leading_rows=1,
    )

    load_job = client.load_table_from_uri(
        gcs_uri, table_ref, job_config=job_config
    )
    load_job.result() 
    print(f"Table {table_id} created with schema from {gcs_uri}.")

def write_to_bq(project_id, dataset_id, table_id, df):
    """Write a Pandas DataFrame to BigQuery."""
    client = bigquery.Client(project=project_id)
    table_ref = client.dataset(dataset_id).table(table_id)

    job = client.load_table_from_dataframe(df, table_ref)
    job.result()  
    print(f"Data written to {dataset_id}.{table_id}")
