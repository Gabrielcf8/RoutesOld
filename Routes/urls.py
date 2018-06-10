from django.conf.urls import url

from Routes.views import ListPoint, CreatePoint, CreateCategory, ListCategory
from . import views

urlpatterns = [
    url(r'^$', views.firstview),
    url(r'^cities', views.cityview),
    url(r'^route', views.routeview),
    url(r'^generate', views.generaterouteview),
    url(r'^categories', views.categoryview),
    url(r'^points', views.pointview),
    url(r'^user_profile/$', views.user_profile),
    url(r'^user_form/$', views.create_profile),
    url(r'^createpoint/$', CreatePoint.as_view(), name='cadastro'),
    url(r'^listpoint/$', ListPoint.as_view(), name='listaPoint'),
    url(r'^createcategory/$', CreateCategory.as_view(), name='cadastro'),
    url(r'^listcategory/$', ListCategory.as_view(), name='lista'),
]
