from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.
def index(request):
    return render(request, 'upload/index.html')

def file(request):
	handle_file_upload(request.FILES['file'])
	return HttpResponseRedirect(reverse('upload:success'))

def success(request):
	return render(request, 'upload/success.html')

def handle_file_upload(f):
    with open(settings.FILE_STORAGE_LOCATION + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)