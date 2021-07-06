from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'mydetails/home.html')

def Education(request):
    return render(request, 'mydetails/educations.html')

def Project(request):
    return render(request, 'mydetails/projects.html')

def Certificate(request):
    return render(request,'mydetails/certificate.html')

def Experience(request):
    return render(request,'mydetails/experience.html')

