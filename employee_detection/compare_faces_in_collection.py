import boto3
import base64

client = boto3.client(
    'rekognition', 
    aws_session_token="", 
    aws_secret_access_key="", 
    aws_access_key_id="", 
    region_name='us-east-1'
)

file = open('Sandeep.jpg', 'rb').read()
CollectionId = "HomeCollection"

response = client.detect_faces(
    Image={
        'Bytes': file
    }
)

if(len(response['FaceDetails']) > 0):
    res = client.search_faces_by_image(
        CollectionId=CollectionId,
        Image={
            'Bytes': file
        }
    )
    print(res['FaceMatches'])
else:
    print('No face detected..')