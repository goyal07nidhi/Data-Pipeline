import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import BytesIO
import boto3
import gzip
from dotenv import load_dotenv
import s3fs

load_dotenv(verbose=True)


def aws_session(region_name='us-east-1'):
    return boto3.session.Session(aws_access_key_id="aws_access_key",
                                 aws_secret_access_key="aws_secret_access",
                                 region_name=region_name)


session = aws_session()
s3 = boto3.client('s3')
archive_url = "https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/"
r = requests.get(archive_url) 
soup = BeautifulSoup(r.content, 'html.parser')
links = soup.findAll('a')
scrape_link = []

for link in links:
    scrape_link.append(link.get_text())
    for i in scrape_link:
        if i.endswith(".csv.gz"):
            filename = i[:-3]
            resp = requests.get(archive_url +i)
            data = resp.content
            gzipfile = BytesIO(data)
            gzipfile = gzip.GzipFile(fileobj=gzipfile)
            content = gzipfile.read().decode("utf-8")
            data1 = content
            df = pd.DataFrame([x.split(',') for x in data1.split('\n')])
            s3 = s3fs.S3FileSystem(anon=False)
            with s3.open('storm-dataset/'+filename,'w') as f:
                df.to_csv(f)