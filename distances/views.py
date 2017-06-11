from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from distances.forms import SearchCriteriaForm
from distances.models import House
from distances.utils import daft_search

from django.contrib import admin


def index(request):
    return HttpResponse("Hello, world. Here you will find useful info soon")


@admin.site.register_view('distances/grabdata', name="Grab Data")
def grabdata(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchCriteriaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            max_price = form.cleaned_data['max_price']
            areas = ','.join(form.cleaned_data['areas'])
            #areas = "blackrock,booterstown,dun-laoghaire,monkstown,sandymount"
            daft_search.extract_and_insert(areas, max_price)
            daft_search.calc_distances()
            # import time
            # time.sleep(10)
            return HttpResponseRedirect('house/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchCriteriaForm()
        data = {
            'user': request.user,
            'opts': House._meta,
            'change': False,
            'add': False,
            'is_popup': False,
            'save_as': False,
            'has_permission': True,
            'has_delete_permission': False,
            'has_add_permission': False,
            'has_change_permission': False,
            'form': form,
        }
    return render(request, 'admin/distances/grabdata.html', data)
