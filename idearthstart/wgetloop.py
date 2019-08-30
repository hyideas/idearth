import wget

def capture():
    url='http://127.0.1.1:8080/?action=snapshot'
    adress='/home/pi/capture.jpg'
    filename=wget.download(url,adress,bar=None)

