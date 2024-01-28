from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return HttpResponse('<h1>Здесь же была ракета!about</h1>')

def rules(request):
    return HttpResponse('<h1>Здесь же была ракета!rules</h1>')