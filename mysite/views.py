from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from distances.forms import NameForm
from distances.models import House
from distances.utils import daft_search

from django.contrib import admin


def index(response):
    return HttpResponseRedirect('admin/')
