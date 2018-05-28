# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from Routes.forms import UserForm, PersonForm
from Routes.models import City, Route, Category, Point


def firstview(request):
    return render(request, 'Routes/user_profile.html')


def cityview(request):
    request_cities = City.objects.all()
    return render(request, 'City/user_profile.html', {'cities': request_cities})


def routeview(request):
    request_routes = Route.objects.all()
    return render(request, 'Route/user_profile.html', {'routes': request_routes})


def categoryview(request):
    request_categories = Category.objects.all()
    return render(request, 'Category/user_profile.html', {'categories': request_categories})


def pointview(request):
    request_points = Point.objects.all()
    return render(request, 'Point/user_profile.html', {'points': request_points})


def user_profile(request):
    return render(request, 'Person/user_profile.html', {})


def create_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        person_form = PersonForm(request.POST, instance=request.user.person)

        if user_form.is_valid() and person_form.is_valid():
            user_form.save()
            person_form.save()
            return render(request, 'Person/user_profile.html', {})
        else:
            print('It is not working!')
    else:
        user_form = UserForm(instance=request.user)
        person_form = PersonForm(instance=request.user.person)

    return render(request, 'Person/person_form.html', {'user_form': user_form, 'person_form': person_form})
