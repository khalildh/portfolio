from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'portfolio/index.html')
def about(request):
    return render(request, 'portfolio/about.html')
def resume(request):
    return render(request, 'portfolio/resume.html')
def portfolio(request):
    return render(request, 'portfolio/portfolio.html')
def contact(request):
    return render(request, 'portfolio/contact.html')
