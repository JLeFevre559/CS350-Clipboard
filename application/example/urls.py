# example/urls.py
from django.urls import path
from example.views import Index, Calendar, Project, Profile

urlpatterns = [
    path('', Index.as_view(), name='Index'),
    path('Calendar',Calendar.as_view(),name='Calendar'),
    path('Project',Project.as_view(),name='Project'),
    path('Profile',Profile.as_view(),name='Profile')
]
