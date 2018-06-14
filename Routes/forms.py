from django import forms
from django.contrib.auth.models import User

from Routes.models import Person, Point, Category, City, Route


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email'}


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = {'birthday', 'biography'}


class PointForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'
