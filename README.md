# Global Sales ETL Pipeline

## Project Overview
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline for a global sales dataset using Python and AWS S3.  
The pipeline moves raw data from a local CSV to AWS S3, transforms it using Python, and stores the cleaned data back in S3 for analytics purposes.

---

## Architecture
Local CSV
↓ (Upload)
S3 Raw Layer
↓ (Python Transform)
S3 Clean Layer

---

## Tech Stack
- **Python** – data processing and scripting
- **Pandas** – data transformation and cleaning
- **AWS S3** – cloud storage for raw and clean datasets
- **Boto3** – AWS SDK for Python
- **GitHub** – version control and project backup

---

## Pipeline Steps

1. **Upload Raw Data**
   - Script: `upload_raw_to_s3.py`  
   - Reads local CSV (`superstore.csv`) and uploads it to S3 raw layer.
2. **Transform Data**
   - Script: `transform_superstore.py`  
   - Reads raw data from S3, performs cleaning and formatting (removing duplicates, standardizing column names, filling missing values), and uploads the cleaned CSV to S3 clean layer.

---

## Folder Structure

global-sales-etl-pipeline/
├── scripts/
│ ├── upload_raw_to_s3.py
│ └── transform_superstore.py
├── data/ (local, not pushed to GitHub)
└── README.md

---

## How to Run

1. Ensure **Python** and **pip** are installed.
2. Install required packages:
   ```bash
   py -m pip install pandas boto3
3. Configure AWS CLI with your IAM user credentials:
   aws configure
4. Upload raw data:
   py scripts\upload_raw_to_s3.py
5. Transform data:
   py scripts\transform_superstore.py

---
Notes

ingestion_date in S3 reflects the date the data was uploaded.

The project currently uses a hardcoded ingestion date (2026-01-06) for demonstration purposes.

Raw data is kept unchanged; all transformations are applied to copies in the clean S3 layer.


