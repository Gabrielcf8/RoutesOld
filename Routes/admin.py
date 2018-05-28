# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from Routes.models import City, Category, Point, Route, Person

admin.site.register(City)
admin.site.register(Category)
admin.site.register(Point)
admin.site.register(Route)
admin.site.register(Person)

