from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time
import googleapiclient
import json
import os

emotionlist = ['anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']
 
try :
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('storage.json')
creds = store.get()

if not creds or creds.invalid:
    print("make new storage data file ")
    flow = client.flow_from_clientsecrets('client_secret_drive.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)

drive_service = build('drive', 'v3', http=creds.authorize(Http()))

FILES = '/home/pi/capture.jpg'
file_name = FILES

def makefolder():
    now=time.localtime()
    log=str(now.tm_year)+'-'+(str(now.tm_mon)+'-'+str(now.tm_mday))+'  '+str(now.tm_hour)+':'+str(now.tm_min)+':'+str(now.tm_sec)
    file_metadata = {'name': log,'mimeType':'application/vnd.google-apps.folder'}

    file = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()
    #print 'File ID: %s' % file.get('id')

    return file.get('id')

def uploadfile(id):
    #upload file to special folder1
    now=time.localtime()
    log=str(now.tm_year)+'-'+(str(now.tm_mon)+'-'+str(now.tm_mday))+'  '+str(now.tm_hour)+':'+str(now.tm_min)+':'+str(now.tm_sec)
    f=open('/home/pi/wget-3.2/php.txt','r')
    line=f.readline()
    f.close()
    s=json.loads(line)
    for emotion in emotionlist:
        flag=float(s[emotion])
        if flag>0.5:
            value=flag
            emo=emotion
            break
        else:
            value=flag
            emo=emotion
            continue
    #if emo=='neutral' and value == 1.0:
    #    os.remove('/home/pi/capture.jpg')
    #    return 1


    print(value,emotion)

    file_metadata = {
        'name': log+' '+emo,
        'parents': [id]
    }

    media = googleapiclient.http.MediaFileUpload(file_name,
                            mimetype='image/jpeg',
                            resumable=True)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    os.remove('/home/pi/capture.jpg')  
    return 0