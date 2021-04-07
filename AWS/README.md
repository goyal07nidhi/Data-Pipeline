# Data pipeline with Snowflake

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

## Table of Contents

- [INTRODUCTION](#INTRODUCTION)
- [ARCHITECTURE](#ARCHITECTURE)
- [SETUP](#SETUP)
- [PROCESS](#PROCESS)
- [REFERENCE](#REFERENCE)

## INTRODUCTION
1. Upload and Store the required data in S3 bucket
2. Create a pipeline using Glue 
3. Write queries in Athena and build visualizations in Amazon Quick sight

## ARCHITECTURE
![image](https://user-images.githubusercontent.com/45726206/110045311-7e80f600-7d18-11eb-9d36-7ca0cba8d270.png)

 
## SETUP
1. Downloading data from AWS s3 bucket requires:

- pip install boto3
- pip install s3fs

2. To web scrape using Beautiful Soup:

- pip install bs4

## PROCESS 

### Data

- Create Access Key in AWS
- Create a Storage Bucket in S3 and upload scrapped Storm data and Sevir data in their respective S3 bucket

#### Create a pipeline using Glue

- In the AWS,  select Glue and schedule a glue job to create a combined dataset and push it into S3 bucket.
- Make use of Glue crawler to fetch the data from S3.
- Once the Crawler is created run it and it will create Glue Datalog and tables.

#### View Query using Athena and Visualize using Quick sight

- Now, make use of Athena by connecting it with table created by crawler and hit queries.
- Lastly, view the result using Amazon Quicksight
	
## REFERENCE

- https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-libraries.html
- https://docs.aws.amazon.com/athena/latest/ug/glue-athena.html
- https://aws.amazon.com/blogs/big-data/accessing-and-visualizing-data-from-multiple-data-sources-with-amazon-athena-and-amazon-quicksight/



