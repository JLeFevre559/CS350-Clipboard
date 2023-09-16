# example/urls.py
from django.urls import path
from example.views import Index

urlpatterns = [
    path('', Index.as_view()),
]
