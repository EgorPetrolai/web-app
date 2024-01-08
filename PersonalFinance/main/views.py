from django.shortcuts import render

def index(request):
    return render(request, 'account/login.html')

def about(request):
    return render(request, 'main/about.html')