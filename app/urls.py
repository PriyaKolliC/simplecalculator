#from django.conf.urls import path
from django.conf.urls import include,url
from . import views

urlpatterns = [
    url('', views.index, name='index'),
	url(r'^thanks/(?P<output>\d+)/$',views.thanks,name='thanks')
]