from django.shortcuts import render
from .models import *
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



