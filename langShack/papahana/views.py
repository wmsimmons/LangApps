from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from .forms import UploadFileForm
#from somewhere import handle_uploaded_file
#from django.utils import timezone

# Create your views here.
def workbench_start(request):

    return render(request, 'workbench-start.html', context=None)

def workbench(request):

    return render(request, 'workbench.html')

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})
