from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.

def homepage(request):
    return render(request, "index.html")

def synthesise(request):
    return render(request, "synthesise.html")

def preview(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('datafilein')
        fs = FileSystemStorage()
        fs.delete('static/media/testimage.png')
        fs.save('static/media/testimage.png', uploaded_file)

    return  render(request,"preview.html")


def GeneratedText(request):
    return render(request, "GeneratedText.html")


def GeneratedImage(request):
    return render(request, "GeneratedImage.html")