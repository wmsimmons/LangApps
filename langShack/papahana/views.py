from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
import csv
from .models import Workbench

# Create your views here.
def workbench_start(request):

    return render(request, 'workbench-start.html', context=None)

def workbench(request):

    return render(request, 'workbench.html')

def simple_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/workbench')
    else:
        form = DocumentForm()
    return render(request, 'workbench-upload.html', {
        'form': form})
