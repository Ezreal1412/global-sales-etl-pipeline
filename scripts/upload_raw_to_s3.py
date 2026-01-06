import boto3
import os
from datetime import date

# Get absolute path to project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCAL_DATA_DIR = os.path.join(PROJECT_ROOT, "data")
S3_BASE_PATH = "raw/global_superstore"

BUCKET_NAME = "azril-global-sales-etl"

s3 = boto3.client("s3")
ingestion_date = date.today().isoformat()

def upload_file(file_name):
    local_path = os.path.join(LOCAL_DATA_DIR, file_name)
    s3_path = f"{S3_BASE_PATH}/ingestion_date={ingestion_date}/{file_name}"

    try:
        s3.upload_file(local_path, BUCKET_NAME, s3_path)
        print(f"✅ Uploaded {file_name} to {s3_path}")
    except Exception as e:
        print(f"❌ Failed to upload {file_name}: {e}")

def main():
    upload_file("superstore.csv")

if __name__ == "__main__":
    main()
