import boto3
import os
import base64
import json

client = boto3.client(
    'rekognition', 
    aws_session_token="", 
    aws_secret_access_key="", 
    aws_access_key_id="", 
    region_name='us-east-1'
)

file = open('me.png', 'rb').read()
response = client.detect_faces(
    Image={
        'Bytes': file
    },
    Attributes=['ALL']
)

for face in response['FaceDetails']:
    print(json.dumps(face, indent=4, sort_keys=True))
