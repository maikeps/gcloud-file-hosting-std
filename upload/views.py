from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'upload/index.html')

def file(request):
    return HttpResponse('Uploaded filename: %s' % request.FILES['file'].name)