from django.conf.urls import url

from . import views

app_name = 'upload'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url('success/', views.success, name='success'),
	url('file/', views.file, name='file'),
]