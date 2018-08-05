from django.conf import settings
from django.core.files.storage import default_storage
from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
def index(request):
	filenames = default_storage.listdir('')[1]
	file_list = [{'filename': filename, 'filesize': default_storage.size(filename)} for filename in filenames]

	return render(request, 'browse/index.html', {'file_list': file_list})

def delete(request):
	checked = request.POST.getlist('file_item')
	for item in checked:
		default_storage.delete(item)

	return render(request, 'browse/delete.html', {'deleted_count': len(checked)})

def download(request, filename):
	if default_storage.exists(filename):
		with default_storage.open(filename, 'r') as f:
			response = HttpResponse(f.read(), content_type='application/force-download')
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filename)
			return response
	else:
		return render(request, 'browse/file_not_found.html', {'filename': filename})