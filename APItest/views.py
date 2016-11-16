# -*- coding: utf-8 -*-
'''
todo
Доделать проверку ответов по GET и DELETE
'''
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.http import HttpResponse;
from models import programms
from serializers import programmSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json


def index(request):

    return render_to_response('index.html');

@api_view(['GET','POST'])
def getAll(request):
    if request.method == 'GET':
        allprogramms = programms.objects.all();
        seriliazedModel = programmSerializer(allprogramms, many=True);
        print(seriliazedModel.data)
        return HttpResponse(json.dumps(seriliazedModel.data))
    if request.method == 'POST':
        rawData = request.body;
        jsonData = json.loads(rawData);
        newProgramm = programms(name =jsonData['name'],coast=jsonData['coast'],description=jsonData['description'])
        print(newProgramm.save())
        return HttpResponse(rawData);



@api_view(['GET','DELETE','POST'])
def getelement(request,pk):
    try:
        currentProgramm = programms.objects.get(id=pk)
    except programms.DoesNotExist:
        return HttpResponse("Not found");

    if request.method == 'GET':
        serializedQuery = programmSerializer(currentProgramm);
        return HttpResponse(json.dumps(serializedQuery.data))
    if request.method == 'DELETE':
        currentProgramm.delete();
        return HttpResponse('Deleted '+ pk);
    if request.method == 'POST':
        jsonData = json.loads(request.body);
        name = currentProgramm.name;
        coast = currentProgramm.coast;
        description = currentProgramm.description;
        if jsonData['name']:
           currentProgramm.name = jsonData['name']
        if jsonData['coast']:
            currentProgramm.coast = jsonData['coast']
        if jsonData['description']:
            currentProgramm.description = jsonData['description']
        try:
           currentProgramm.save()
           return HttpResponse(status=201)
        except Exception:
           return HttpResponse("faild")
        #else:
        #    return HttpResponse(status=403);
# Create your views here.

def rowCount(request):
    count = programms.objects.count();
    return HttpResponse(count);