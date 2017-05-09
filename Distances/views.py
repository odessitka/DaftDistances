from django.shortcuts import render
from django.http import HttpResponse

from Distances.utils import daft_search


def index(request):
    return HttpResponse("Hello, world. Here you will find useful info soon")
# Create your views here.


def grabdata(request):
    daft_search.main()
    return  HttpResponse("data grabbed!!!")