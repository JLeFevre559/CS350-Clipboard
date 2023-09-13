# example/views.py
from datetime import datetime
from django.views.generic import TemplateView
from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = '_navbar.html'

def index(request):
    now = datetime.now()
    html = f"""
    <html>
        <body>
            <h1>Hello from Clipboard!</h1>
            <h1>This is the hosted website for the TaskBoard team from UNCO for CS350</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    """
    return HttpResponse(html)
