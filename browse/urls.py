from django.conf.urls import url

from . import views

app_name = 'browse'
urlpatterns = [
	url('delete/', views.delete, name='delete'),
	url(r'^download/(?P<filename>.*)/$', views.download, name='download'),
	url('^$', views.index, name='index'),
]