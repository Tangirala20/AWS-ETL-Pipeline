Overview
This project implements a serverless ETL (Extract, Transform, Load) pipeline using AWS services. Raw data is uploaded to an S3 bucket and a Lambda function is triggered to process the data. After successful transformation, the output is saved back into a destination S3 bucket. An SNS notification is sent if any abnormal activity or data issue is detected during the process.

 Architecture
Source S3 Bucket — Raw data (CSV, JSON, etc.) is uploaded here.
AWS Lambda — Triggered by S3 event; parses, validates, and transforms the incoming data.
Amazon SNS — Sends a notification if abnormal activity or data inconsistencies are detected.
Destination S3 Bucket — Stores the cleaned and transformed data for downstream use.

Workflow
Upload Raw Data — A new file is uploaded to the source S3 bucket.
Trigger Lambda — S3 event invokes the Lambda function.
Data Processing — Lambda validates and transforms the data.
Abnormal Activity Check — Lambda identifies anomalies (e.g., missing fields, invalid types) and publishes an alert to an SNS topic.
Store Output — The successfully processed file is saved to the destination S3 bucket.

Technologies
AWS S3 — Storage for input and output datasets.
AWS Lambda — Serverless compute for data extraction and transformation.
Amazon SNS — Notification service for abnormal activity or errors.
Python (Boto3) — Language and AWS SDK for writing the Lambda function.
