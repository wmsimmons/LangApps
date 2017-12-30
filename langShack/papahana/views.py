from django.shortcuts import render
#from django.utils import timezone

# Create your views here.
def default_workbench(request):

    return render(request, 'workbench.html', context=None)
