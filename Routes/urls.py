from django.conf.urls import url

from Routes.views import ListPoint, CreatePoint, CreateCategory, ListCategory, ListCity, CreateCity, CreateRoute, \
    ListRoute
from . import views

urlpatterns = [
    url(r'^$', views.firstview),
    url(r'^cities', views.cityview),
    url(r'^route', views.routeview),
    url(r'^generate', views.generaterouteview),
    url(r'^categories', views.categoryview),
    url(r'^points', views.pointview, name='points'),
    url(r'^map', views.mapview),
    url(r'^user_profile/$', views.user_profile),
    url(r'^user_form/$', views.create_profile),
    url(r'^createpoint/$', CreatePoint.as_view(), name='cadastroPoint'),
    url(r'^listpoint/$', ListPoint.as_view(), name='listaPoint'),
    url(r'^createcategory/$', CreateCategory.as_view(), name='cadastroCategory'),
    url(r'^listcategory/$', ListCategory.as_view(), name='listaCategory'),
    url(r'^createcity/$', CreateCity.as_view(), name='cadastroCity'),
    url(r'^listcity/$', ListCity.as_view(), name='listaCity'),
    url(r'^createroute/$', CreateRoute.as_view(), name='cadastroRoute'),
    url(r'^listroute/$', ListRoute.as_view(), name='listaRoute'),
]
