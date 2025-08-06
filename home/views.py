# home/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("🚀 Hello from Railway + Django App!")
