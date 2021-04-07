import pandas as pd
import boto3
import s3fs


def aws_session(region_name='us-east-1'):
    return boto3.session.Session(aws_access_key_id="aws_access_key",
                                 aws_secret_access_key="aws_secret_access",
                                 region_name=region_name)


bucket = 'sevir-demo' 
startAfter = 'CATALOG.csv'  
session = aws_session()
conn = boto3.client('s3')
s3 = boto3.resource('s3')


response = conn.list_objects(Bucket="storm-data-team6")

df_list = []
itr = 0
for file in response["Contents"]:

    obj = conn.get_object(Bucket="storm-data-team6", Key=file["Key"])
    df_obj= pd.read_csv(obj["Body"],encoding="utf8")
    df_obj = df_obj.loc[:, ~df_obj.columns.str.contains('^Unnamed')]
    new_header = df_obj. iloc[0]
    df_obj = df_obj[1:]
    df_obj.columns = new_header 
    df_list.append(df_obj)
    itr+=1

    if itr == 20:
        break
    
df = pd.concat(df_list)
df = df.dropna(axis=1,how='all')
print(df.info())
print(df.shape)
s3 = s3fs.S3FileSystem(anon=False)
with s3.open('storm-data-combined/'+'combined_results_after_scrapping.csv', 'w') as f:
    df.to_csv(f)
