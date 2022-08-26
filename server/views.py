from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("Hello DJango!");

def test2(request):
    return HttpResponse("Implement what you want!");