#-*-coding: utf-8 -*-
'''
**********************************************************************
* Filename    : viewsws
* Description : views for server
* Author      : Sangyun.Kwon
* Brand       : MagicEco
* Website     : www.magice.co
* Update      : Sangyun.Kwon    2019-03-24    New release
**********************************************************************
'''

from django.shortcuts import render_to_response
from django.http import HttpResponse
import os
from remote_control.driver import stream
import pickle
import requests
import json
import threading
import time
import subprocess
import urllib
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

print stream.start()

def home(request):
    host = stream.get_host().split(' ')[0]
    return render_to_response("run.html", {'host': host})

def run(request):
    if 'action' in request.GET:
        action = request.GET['action']
        if action == 'emotion':
            return render_to_response("output.html")
        elif action == 'youtube':
            title = request.GET['title']
            print(title)
            youtubeThread = threading.Thread(target=TurnOnYoutube, args=(title,))
            youtubeThread.daemon = True
            youtubeThread.start()
            

    return render_to_response("base.html")

def connection_test(request):
    return HttpResponse('OK')

def TurnOnYoutube(title):
    key = 'AIzaSyASzEbK71cR11YGpA9N2Wzjc9gZTB2HHtc'
    print('1:'+title)
    print(type(title))
    title = {'' : title}
    print('1.5')
    title = urllib.urlencode(title)[1:]
    print('2:'+title)
    url = 'https://www.googleapis.com/youtube/v3/search?key='+key+'&part=id&q='+title+'&order=relevance&type=video'
        
    response = requests.get(url)

    json_data = json.loads(response.text)

    youtube_id = json_data["items"][1]["id"]["videoId"]
    Proc = subprocess.check_output("pgrep -lf chromium*", shell=True)
    pid = ""
    for list in Proc.split('\n'):
        if 'chromium' in list:
            pid = list
    if pid != "":
        os.system("kill " + pid.split(' ')[0])
        os.system('chromium-browser --start-fullscreen --fast-start --app=https://www.youtube.com/embed/'+youtube_id+'?autoplay=1&rel=0&vq=large')
        time.sleep(15)
    else:
        os.system('chromium-browser --start-fullscreen --fast-start --app=https://www.youtube.com/embed/'+youtube_id+'?autoplay=1&rel=0&vq=large')
        time.sleep(25)
    
    os.system('xdotool mousemove 300 300')
    os.system('xdotool click 1')
