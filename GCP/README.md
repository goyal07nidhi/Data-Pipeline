# Data Pipeline with GCP

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


# Table of Contents

- [Introduction](#Introduction)
- [Architecture](#Architecture)
- [Process](#Process)
- [References](#References)
---

# Introduction
In this Assignment, we are trying to, 
1. Upload and Store the required data in Google Cloud Storage 
2. Create a pipeline using Dataflow to load the data in Google BigQuery tables
3. Write queries in Google BigQuery and build visualizations in Google Data Studio

# Architecture
![GCP Architecture (1)](https://user-images.githubusercontent.com/33648410/110011898-ee2dbb80-7ced-11eb-9c6b-0a2e49658f97.png)

# Process
## 1. Upload the data to Google Cloud Storage
1. Create a Storage Bucket in GCP
2. Create a Service Account in (IAM & Admin/Service Accounts) and then download the key which is in the json format
3. ```pip install --upgrade google-cloud-storage``` and run the upload_to_gcp.py file by replacing the location of json file, storage bucket name, location of the file to be fetched and location of file in the GCS where the data should be stored
5. The required files will get uploaded in GCS

## 2. Create a pipeline using Dataflow to load the data in Google BigQuery tables
### 1. Pre-requsites
1. In the Google Cloud Console, on the project selector page, select or create a Google Cloud project.
2. Make sure that billing is enabled for your Cloud project.
3. Enable the BigQuery, AI Platform, Cloud Source Repositories, Dataflow, and Datalab APIs.

### 2. Launch the DataLab
1. Open Cloud Shell and run the following command to set the project 

```gcloud config set project [PROJECT_ID]```

2. Run the following command to retrieve the Project

```gcloud config list project --format "value(core.project)"```

3. Create a Datalab instance

```datalab create --zone us-central1-a mydatalab```

Note: To use the same instance next time, ```run datalab connect mydatalab```.

4. Click Cloud Shell Web preview in Cloud Shell to launch the Datalab notebook listing page.
5. Select Change port and click Port 8081 to open a new tab in your browser.

### 3. Creating a pipeline using DataFlow to fetch the data from GCS and move it to BigQuery
1. After launching the DataLab run the GCP_DataFlow_Pipeline script 
2. The Pipeline can be seen in the DataFlow section in GCP and the status of the pipeline

## 3. Write queries in Google BigQuery and build visualizations in Google Data Studio
1. We can now see the data in the tables created in the pipeline and query to get the results required
2. In Google Data Studio, click on add data and select BigQuery to get the required tables 
3. Make the Dashboard

Link: https://datastudio.google.com/u/0/reporting/6e36cc27-e89a-496d-82db-143142072dd3/page/tAp4B

![image](https://user-images.githubusercontent.com/33648410/110012005-0ac9f380-7cee-11eb-8788-6a4b08441149.png)

# References
1. https://cloud.google.com/bigquery/docs/visualize-data-studio
2. https://cloud.google.com/solutions/machine-learning/ml-on-structured-data-analysis-prep-1
3. https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python
4. https://towardsdatascience.com/apache-beam-pipeline-for-cleaning-batch-data-using-cloud-dataflow-and-bigquery-f9272cd89eba


