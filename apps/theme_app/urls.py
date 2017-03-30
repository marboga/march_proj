from django.conf.urls import url

from . import views

app_name = "theme_app"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^process$', views.process, name="process"),
    url(r'^lockbox$', views.lockbox, name="lockbox"),
    url(r'^activity/create$', views.create_activity, name="create_activity"),
    url(r'^activity/(?P<id>\d+)$', views.show, name="show"),
    url(r'^create_user$', views.create_user, name="create_user"),
]
