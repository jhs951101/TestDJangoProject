from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def setUserInfo(result):
    result['name'] = '심지훈'
    result['age'] = 25
    return result

@csrf_exempt
def get(request):
    result = {}
    result['success'] = False

    username = request.GET.get('username', None)
    password = request.GET.get('password', None)

    if username is not None and password is not None:
        result = setUserInfo(result)
        result['success'] = True

    return HttpResponse(json.dumps(result, ensure_ascii=False))

@csrf_exempt
def post(request):
    result = {}
    result['success'] = False

    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    if username is not None and password is not None:
        result = setUserInfo(result)
        result['success'] = True
    
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@csrf_exempt
def postjson(request):
    result = {}
    result['success'] = False

    username = None
    password = None

    data = json.loads(request.body)

    if 'username' in data.keys():
        username = data['username']
    
    if 'password' in data.keys():
        password = data['password']

    if username is not None and password is not None:
        result = setUserInfo(result)
        result['success'] = True
    
    return HttpResponse(json.dumps(result, ensure_ascii=False))