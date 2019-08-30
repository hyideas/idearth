import requests
import json
import sys

def azurl():
    
    str_get='/home/pi/capture.jpg'
    subscription_key = '6a7572bd3f4d4fcca28ffc6ecb6d25de'
    assert subscription_key == '6a7572bd3f4d4fcca28ffc6ecb6d25de'

    face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type':'application/octet-stream'}
    data=open(str_get,'rb').read()
    
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'emotion',
    }
    
    response = requests.post(face_api_url, params=params,
                          headers=headers, data=data)
    
    f=open('/home/pi/wget-3.2/output.txt','w')
    text=json.dumps(response.json())
    f.write(text)
    f.close()