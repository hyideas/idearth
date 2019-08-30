import requests
import json
import wgetloop
import azure_income
import time
import os
import change_new
import Googledrive
import time
import phptest
import sense
import threading
count=0

def getHumidityTemperature():
    global bhumidity
    global btemperature
    try:
        bhumidity, btemperature = sense.getHumidityTemperature()
    except:
        bhumidity = -1.0
        btemperature = -1.0
    #print("Threading")
    return bhumidity, btemperature

print("callibration")
bhumidity, btemperature= sense.getHumidityTemperature()
print("callibration complete!")
id=Googledrive.makefolder()
print("Album maked!\n")


while True:
    t1 = threading.Thread(target = getHumidityTemperature)
    t1.start() 
    now=time.localtime()
    print('Exexcution Number is '+str(count+1)+"th")
    count+=1
    print('The time log is '+str(now.tm_year)+'-'+(str(now.tm_mon)+'-'+str(now.tm_mday))+'  '+str(now.tm_hour)+':'+str(now.tm_min)+':'+str(now.tm_sec))
    wgetloop.capture()
    
    azure_income.azurl()
    print('Emotion Cognition is executed by using Azure. We used FACE cognition API. It is AI for Emotion.')
    bhumidity, btemperature=change_new.parsing(bhumidity,btemperature)
    print(bhumidity,btemperature)
    print('Sensor Cognition is executed by using DHT11 & PCF8692 & Sound sensor. Furthermore, Those things are connected to Raspberry pi 3b+ GPIO module.')
    flag=Googledrive.uploadfile(id)
    #if flag==1:
    #    continue
    print('Album File Uploaded to Google drive. You can check photo files by just using smartphone.')
    phptest.php()
    print('DB Stored. The data is Sensor for kids environment and Emotion cognition for kids face.\n DB is executed by using AWS EC2 Server.')
    
    print("\n")
    print('Machine Learning started! Gradient Descent was used to analysis mentioned data.')
    
    
    
