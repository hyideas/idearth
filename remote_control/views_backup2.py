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
from bs4 import BeautifulSoup


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
            title = request.GET.get('title', '')
            print('1')
            response = requests.get('https://www.youtube.com/results?search_query='+title)
            print('2')
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find_all('div', { 'class': 'yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix' })
            output = ""
            line = str(list(table)[0])
            num=(line.find('data-context-item-id'))
            print('3')
            while True:
                if line[num+22] == '"':
                    break
                output += line[num+22]
                num += 1
            print(output)
            os.system('chromium-browser --app=https://www.youtube.com/embed/'+output+'?autoplay=1&rel=0&vq=large --new-window')

    return render_to_response("base.html")

def connection_test(request):
    return HttpResponse('OK')

