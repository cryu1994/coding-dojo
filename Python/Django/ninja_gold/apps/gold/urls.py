from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^process_money$', views.process),
	url(r'^start_over', views.reset)
]