from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^lockbox$', views.lockbox),
    url(r'^activity/create$', views.create_activity),
]
