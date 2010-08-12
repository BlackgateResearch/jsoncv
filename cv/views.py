from django.http import Http404,HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from couchdb import Server
from couchdb.http import ResourceNotFound
import json

SERVER = Server('http://127.0.0.1:5984')
if (len(SERVER) == 0):
    SERVER.create('cvs')
    

def detail(request,id):
    cvs = SERVER['cv']
    try:
        cv = cvs[id]
    except ResourceNotFound:
        raise Http404        
    if request.method =="POST":
        cv['title'] = request.POST['title'].replace(' ','')
        cv['text'] = request.POST['text']
        cvs[id] = cv
#    return render_to_response('couch_cvs/detail.html',{'row':cv})
    return HttpResponse(json.dumps(cv))
