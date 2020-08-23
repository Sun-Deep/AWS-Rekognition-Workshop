import boto3

client = boto3.client(
    'rekognition', 
    aws_session_token="", 
    aws_secret_access_key="", 
    aws_access_key_id="", 
    region_name='us-east-1'
)

response = client.create_collection(
    CollectionId = "HomeCollection"
)

print(response)