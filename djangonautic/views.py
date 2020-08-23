from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    #return HttpResponse("Hello this is the about page")
    return render(request, 'about.html')

def home(request):
    #return HttpResponse("homepage")
    return render(request, 'homepage.html')