from django.shortcuts import render
from django.shortcuts import render

def home(request):
    return render(request, 'app1/home.html')

# Create your views here.
