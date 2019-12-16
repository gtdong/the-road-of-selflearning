from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
# Create your views here.


def index(request):
    return HttpResponse('app02 index')