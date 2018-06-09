from django import forms
from django.contrib.auth.models import User

from Routes.models import Person, Point, Category


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
