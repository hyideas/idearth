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
#from driver import stream
from django.http import HttpResponse
import os
from remote_control.driver import stream
import pickle



print stream.start()

def home(request):


    host = stream.get_host().split(' ')[0]
    return render_to_response("run.html", {'host': host})

def run(request):
  
    if 'action' in request.GET:
        return render_to_response("output.html")
    return render_to_response("base.html")
def connection_test(request):
	return HttpResponse('OK')
