from google.cloud import storage
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '' #give the location of key json file ' 

storage_client = storage.Client()
buckets = list(storage_client.list_buckets())
bucket = storage_client.get_bucket("") # give your storage bucket name

print('Start')


def upload_catalogcsv():
	blob = bucket.blob('/Data/CATALOG.csv')
	blob.upload_from_filename('filepath')
	print('upload catalog csv complete')


def upload_stormcsv():
	blob = bucket.blob('/Data/StormEvents_Loc.csv')
	blob.upload_from_filename('filepath')
	print('upload storm csv complete')


upload_catalogcsv()
upload_stormcsv()






