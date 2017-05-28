from django.shortcuts import render
from django.http import HttpResponse

from .models import Shack

# Create your views here.
def shack_list(request):
	shacks = Shack.objects.all()
	return render(request, 'xacatlahtolli/shack_list.html', {'shacks': shacks})