# example/urls.py
from django.urls import path

from example.views import landing


urlpatterns = [
    path("", landing),
]
