from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Projects

# Create your views here.
def home(request):
    return render(request, 'home.html')

def ourMission(request):
    return render(request, 'ourmission.html')