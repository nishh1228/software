from django.shortcuts import render
from django.shortcuts import render

def sample_page(request):
    return render(request, 'app2/sample.html')

# Create your views here.
