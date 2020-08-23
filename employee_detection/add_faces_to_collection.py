import boto3

client = boto3.client(
    'rekognition', 
    aws_session_token="", 
    aws_secret_access_key="", 
    aws_access_key_id="", 
    region_name='us-east-1'
)

file = open('keki.png', 'rb').read()
CollectionId = "HomeCollection"

response = client.index_faces(
    CollectionId=CollectionId,
    Image={
        'Bytes': file
    },
    ExternalImageId="KekiAdhikari"
)

print(response)

