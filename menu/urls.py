from django.conf.urls import url

from . import views

app_name = 'menu'
urlpatterns = [
	url('', views.index, name='index')
]