# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from Routes.forms import UserForm, PersonForm, PointForm, CategoryForm, CityForm, RouteForm
from Routes.models import City, Route, Category, Point


# Create your views here.


def firstview(request):
    return render(request, 'Routes/index.html')


def cityview(request):
    request_cities = City.objects.all()
    return render(request, 'City/index.html', {'cities': request_cities})


def routeview(request):
    request_routes = Route.objects.all()
    return render(request, 'Route/index.html', {'routes': request_routes})


def categoryview(request):
    request_categories = Category.objects.all()
    return render(request, 'Category/index.html', {'categories': request_categories})


def pointview(request):
    request_points = Point.objects.all()
    return render(request, 'Point/index.html', {'points': request_points})


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


def generaterouteview(request):
    return render(request, 'Route/generate.html', {})


def mapview(request):
    return render(request, 'Point/map.html', {})


def pointadmin(request):
    return render(request, 'index.html')


class CreatePoint(CreateView):
    template_name = 'cadastro.html'
    model = Point
    success_url = reverse_lazy('lista')
    form_class = PointForm


class ListPoint(ListView):
    template_name = 'Point/index.html'
    model = Point
    context_object = 'nome'


def categoryadmin(request):
    return render(request, 'index.html')


class CreateCategory(CreateView):
    template_name = 'cadastro.html'
    model = Category
    success_url = reverse_lazy('lista')
    form_class = CategoryForm


class ListCategory(ListView):
    template_name = 'lista.html'
    model = Category
    context_object = 'nome'


class CreateCity(CreateView):
    template_name = 'cadastro.html'
    model = City
    success_url = reverse_lazy('lista')
    form_class = CityForm


class ListCity(ListView):
    template_name = 'lista.html'
    model = City
    context_object = 'nome'


class CreateRoute(CreateView):
    template_name = 'cadastro.html'
    model = Route
    success_url = reverse_lazy('lista')
    form_class = RouteForm


class ListRoute(ListView):
    template_name = 'lista.html'
    model = Route
    context_object = 'nome'