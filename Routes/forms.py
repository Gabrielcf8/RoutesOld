from django import forms
from django.contrib.auth.models import User

from Routes.models import Person


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email'}


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = {'birthday', 'biography'}
