import boto3
import sys
import json
import base64


def lambda_handler(event, context):

  client = boto3.client('rekognition')

  payload_dict = json.loads(json.loads(event['body']))
  selfie = payload_dict['selfie']
  dl = payload_dict['dl']

  # convert text to base64
  s_base64 = selfie.encode('utf-8')
  t_base64 = dl.encode('utf-8')
  #convert base64 to bytes
  s_bytes = base64.b64decode(s_base64)
  t_bytes = base64.b64decode(t_base64)
  response = client.compare_faces(SimilarityThreshold=80,
                                SourceImage={'Bytes': s_bytes},
                                TargetImage={'Bytes': t_bytes})

  for faceMatch in response['FaceMatches']:
      position = faceMatch['Face']['BoundingBox']
      similarity = str(faceMatch['Similarity'])

  return {

    'statusCode': response['ResponseMetadata']['HTTPStatusCode'],

    'body': similarity

  }
