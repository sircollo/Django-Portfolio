from django.shortcuts import render,Http404
from .models import *
DoesNotExist = Http404
# Create your views here.
from django.http  import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    abouts =About.my_abouts()
    return render(request, 'about.html', {'abouts':abouts})

def projects(request):
    projects = Project.my_projects()
    return render(request, 'projects.html',{'projects':projects})

def project(request,pk):
    try:
        project = Project.objects.get(id=pk)
    except DoesNotExist:
        raise Http404()
    return render(request,"project.html", {"project":project})


