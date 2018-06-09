# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class City(models.Model):
    INITIAL_ID = 1

    Name = models.CharField(max_length=150)
    Photo = models.ImageField(blank=True, null=True)
    State = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)

    def __unicode__(self):
        return self.Name


class Category(models.Model):
    INITIAL_ID = 1

    Name = models.CharField(max_length=150)
    Description = models.CharField(max_length=350)
    Photo = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return self.Name


class Point(models.Model):
    INITIAL_ID = 1

    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    Photo = models.ImageField(blank=True, null=True)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Category = models.ForeignKey(Category, default=INITIAL_ID, on_delete=models.CASCADE)
    City = models.ForeignKey(City, default=INITIAL_ID, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.Name


class Route(models.Model):
    INITIAL_ID = 1

    Name = models.CharField(max_length=150)
    Photo = models.ImageField(blank=True, null=True)
    City = models.ForeignKey(City, default=INITIAL_ID, on_delete=models.CASCADE)
    Points = models.ManyToManyField(Point)

    def __unicode__(self):
        return self.Name


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    biography = models.TextField(max_length=300, blank=True)

    def __unicode__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_person(sender, instance, created, **kwargs):
        if created:
            Person.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_person(sender, instance, **kwargs):
        instance.person.save()
