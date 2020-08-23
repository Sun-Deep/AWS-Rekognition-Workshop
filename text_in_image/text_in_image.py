import boto3
import base64
import json

client = boto3.client(
    'rekognition', 
    aws_session_token="", 
    aws_secret_access_key="", 
    aws_access_key_id="", 
    region_name='us-east-1'
)

file = open('text.jpg', 'rb').read()
response = client.detect_text(
    Image={
        'Bytes': file
    },
)

# print(response['TextDetections'])
texts = []

for text in response['TextDetections']:
    if text['Type'] == 'WORD':
        texts.append(text['DetectedText'])

print(" ".join(texts))
# for face in response['FaceDetails']:
#     print(json.dumps(face, indent=4, sort_keys=True))
