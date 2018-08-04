from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
import os

# Create your views here.
def index(request):
	file_list = os.listdir(settings.FILE_STORAGE_LOCATION)
	return render(request, 'browse/index.html', {'file_list': file_list})

def delete(request):
	checked = request.POST.getlist('file_item')
	files = ''
	for item in checked:
		os.remove(os.path.join(settings.FILE_STORAGE_LOCATION, item))

	return HttpResponse('%d files removed.' % len(checked))

def download(request, filename):
	filepath = os.path.join(settings.FILE_STORAGE_LOCATION, filename)
	if os.path.exists(filepath):
		with open(filepath, 'rb') as f:
			response = HttpResponse(f.read(), content_type='application/force-download')
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filepath)
			return response
	raise Http404