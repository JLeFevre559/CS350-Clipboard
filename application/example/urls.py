# example/urls.py
from django.urls import path
from example.views import index, IndexView

urlpatterns = [
    path('', index),
    path('_navbar', IndexView.as_view()),
]
