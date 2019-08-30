import requests
import json

def php():
    
    URL = 'http://ec2-3-17-158-59.us-east-2.compute.amazonaws.com/ConnectDB.php'
    f=open('/home/pi/wget-3.2/php.txt','r')
    line=f.readline()
    f.close
    # json data
    #payload={'temperature':'26.000000','light':'17.000000','humidity':'78.000000','sound':'19.000000','anger':'0.0','contempt':'0.0','disgust':'0.0','fear':'0.0','happiness':'0.0','neutral':'1.0','sadness':'0.0','surprise':'0.0'}
    
    #ppayload = {'NAME':'ebi'}
    
    headers = {'content-type': 'application/json'}
 
    # post to url 
    response = requests.post(URL, data=line, headers=headers)
    
    
    # result value
    print(response.status_code )
    data = response.text
    print(data)
    #jsondata = response.json()
    #print(jsondata)
    
    #write result
    #f = open("./response.txt", "w+")
    #f.write(str(data))    
    #f.close()