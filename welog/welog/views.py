from django.shortcuts import render
from django.http import HttpResponse
app_name="index"
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
