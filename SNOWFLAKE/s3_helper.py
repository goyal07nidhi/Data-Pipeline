import boto3
import s3fs

class S3Helper:
    _instance = None
    _s3_client = None
    _s3fs_client = None

    def __init__(self):
        raise RuntimeError("Use instance()")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._s3_client = boto3.resource(service_name='s3',
                                            region_name='us-east-1')
            cls._s3fs_client = s3fs.S3FileSystem(anon=False)

        return cls._instance

    def download_file(self, bucket, download_file_name, file_name):
        self._s3_client.Bucket(bucket).download_file(Key=file_name, Filename=download_file_name)
        print("Downloading in process!")

    def upload_dataframe(self, bucket, filename, dataframe):
        with self._s3fs_client.open(bucket + "/Assignment-1/" + filename, 'w') as f:
            dataframe.to_csv(f)
