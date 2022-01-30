import json
import boto3
import logging
import uuid

log = logging.getLogger('__lambda_handler__')

def lambda_handler(event, context):
    log.setLevel(level=logging.INFO)    
    log.info('lambda_handler triggered')
    
    s3_client = boto3.client('s3')
    bucket_name = 'xw-cloudtask-ali-kazim'

    try:
        bucket_response = get_bucket_content(s3_client, bucket_name)
        response_object = prepare_response(bucket_response)
    except Exception as e:
        log.error('Execpution while preparing the GET response : ' + str(e))

    return response_object          

def get_bucket_content(s3_client, bucket_name):
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    s3_files = response["Contents"]
    file_content =''
    bucket_response = []
    
    for s3_file in s3_files:
        bucket_content = {}
        file_content = s3_client.get_object(Bucket=bucket_name,Key=s3_file["Key"])["Body"].read()
        bucket_content.update({'object-name' : s3_file["Key"] , 'content' : str(file_content)})
        bucket_response.append(bucket_content)
        
    bucket_api_response = {}
    bucket_api_response['response_id'] = str(uuid.uuid4())
    bucket_api_response['bucket_response'] = bucket_response
    
    return bucket_api_response
    
def prepare_response(bucket_response):
    response_object = {}
    response_object['statusCode'] = 200
    response_object['headers'] = {}
    response_object['headers']['Content-Type'] = 'application/json'
    response_object['body'] = json.dumps(bucket_response)