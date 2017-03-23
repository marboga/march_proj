from django.conf.urls import url

from . import views

app_name = "languages_app"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^process$', views.process, name="process"),
    url(r'^new$', views.new, name="new"),
]
