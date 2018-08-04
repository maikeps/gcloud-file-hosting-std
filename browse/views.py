from django.conf import settings
from django.core.files.storage import default_storage
from django.http import HttpResponse, Http404
from django.shortcuts import render
import os

# Create your views here.
def index(request):
	file_list = default_storage.listdir('')[1]
	return render(request, 'browse/index.html', {'file_list': file_list})

def delete(request):
	checked = request.POST.getlist('file_item')
	for item in checked:
		default_storage.delete(item)

	return HttpResponse('%d files removed.' % len(checked))

def download(request, filename):
	if default_storage.exists(filename):
		with default_storage.open(filename, 'r') as f:
			response = HttpResponse(f.read(), content_type='application/force-download')
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filename)
			return response
	raise Http404