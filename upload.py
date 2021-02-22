import boto3
from botocore.exceptions import NoCredentialsError
import key as config

ACCESS_KEY = config.accesKey
SECRET_KEY = config.accesSecret


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = upload_to_aws('3.PNG', 'mytextextract', '3.png')

def delete_from_s3(bucket, model):
    try:
        s3 = boto3.client(
            "s3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY
        )
        s3.delete_object(Bucket=bucket, Key=model)
        return True
    except Exception as ex:
        print(str(ex))
        return False

#delete_from_s3('mytextextract', 'up.jpg')

def dl(bucket, key, model_path):
    try:
        s3 = boto3.client(
            "s3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY
        )
        s3.download_file(bucket, key, model_path)
    except Exception as ex:
        print(str(ex))
        return False
    return True

#dl('mytextextract', '3.png', '/')

