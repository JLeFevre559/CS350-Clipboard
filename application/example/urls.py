# example/urls.py
from django.urls import path, include
from example.views import Index, Calendar, Project, Profile, CustomLoginView, SignupView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Index.as_view(), name='Index'),
    path('Calendar',Calendar.as_view(),name='Calendar'),
    path('Project',Project.as_view(),name='Project'),
    path('Profile',Profile.as_view(),name='Profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
