# example/views.py
from datetime import datetime
from django.views.generic import TemplateView
from django.http import HttpResponse

class Index(TemplateView):
    template_name = 'TempHome.html'

class Calendar(TemplateView):
    template_name = 'Calendar.html'

class Project(TemplateView):
    template_name = 'Project.html'

class Profile(TemplateView):
    template_name = 'Profile.html'
