import datetime
import logging
import os

import boto3
import pytz

logging.basicConfig(level=logging.INFO)


class S3FileDownloader:
    """S3 file downloader"""

    def __init__(self, bucket_name: str, local_folder: str):
        """
        Args:
            bucket_name (str): Name of the S3 bucket
            local_folder (str): Local folder where the files will be downloaded
        """
        self.bucket_name = bucket_name
        self.local_folder = local_folder
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        )
        self.timezone = pytz.timezone("America/New_York")

    def download_file(self, s3_key: str):
        """
        Download a file from S3. Otherwise, copy it from the local path

        Args:
            s3_key (str): Key of the file in S3
        """
        response = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=s3_key)

        if not os.path.exists(self.local_folder):
            os.mkdir(self.local_folder)

        if "Contents" in response:
            for obj in response["Contents"]:
                if s3_key in obj["Key"]:
                    s3_file_last_modified = obj["LastModified"]

        file_path = os.path.join(self.local_folder, s3_key.split("/")[-1])

        if os.path.exists(file_path):
            local_file_last_modified = datetime.datetime.fromtimestamp(
                os.path.getmtime(file_path)
            )
        else:
            local_file_last_modified = ""

        if not local_file_last_modified or local_file_last_modified.astimezone(
            self.timezone
        ) < s3_file_last_modified.astimezone(self.timezone):
            try:
                self.s3.download_file(
                    self.bucket_name,
                    s3_key,
                    f"{self.local_folder}/{s3_key.split('/')[-1]}",
                )
                logging.info(f"File {s3_key} downloaded from S3")
            except Exception as e:
                logging.exception(e)


if __name__ == "__main__":
    a = S3FileDownloader(bucket_name="mlops-task", local_folder="data/scripts")
    a.download_file("script_1.py")
