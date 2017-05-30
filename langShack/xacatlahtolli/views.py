from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Projects

# Create your views here.
def projects(request):
	projects = Projects.objects.all()
	return render(request, 'projects.html', {'projects': projects})