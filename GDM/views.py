from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from projects.models import Projects

def Home(request):

    return render(request,"Home.html")

def aboutUs(request):
    return render(request,"aboutUs.html")

def services(request):
    return render(request,"services.html")

def projects(request):
    ProjectData=Projects.objects.all()
    data={
        'ProjectData':ProjectData
    }
    return render(request,"projects.html",data)

def contact(request):
    return render(request,"contact.html")