from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UploadForm


# Create your views here.
def index(request):
    return render(request, 'upload/index.html', {'form': UploadForm()})

def file(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			handle_file_upload(request.FILES['file'])
			return HttpResponseRedirect(reverse('upload:success'))
	else:
		form = UploadForm()
	return render(request, 'upload/index.html', {'form': form})

def success(request):
	return render(request, 'upload/success.html', {})

def handle_file_upload(f):
	with default_storage.open(f.name, 'w') as uploaded_file:
		# Chunks of 64Kb
		for chunk in f.chunks():
			uploaded_file.write(chunk)