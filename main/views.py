from django.shortcuts import render
from .models import *
# Create your views here.
from django.http  import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.my_projects()
    return render(request, 'projects.html',{'projects':projects})



