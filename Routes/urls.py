from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.firstview),
    url(r'^cities', views.cityview),
    url(r'^routes', views.routeview),
    url(r'^categories', views.categoryview),
    url(r'^points', views.pointview),
    url(r'^user_profile/$', views.user_profile),
    url(r'^user_form/$', views.create_profile),
]