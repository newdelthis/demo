import boto3
import urllib.parse

s3 = boto3.client('s3')
target_bucket_name = 'YOUR_TARGET_BUCKET_NAME'  # Replace with your target bucket name

def lambda_handler(event, context):
    source_bucket_name = ‘YOUR_SOURCE_BUCKET_NAME’
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    try:
        copy_source = {'Bucket': source_bucket_name, 'Key': key}
        s3.copy(copy_source, target_bucket_name, key)
        print(f"Successfully copied {key} from {source_bucket_name} to {target_bucket_name}")
    except Exception as e:
        print(f"Error copying {key}: {e}")
        raise e
