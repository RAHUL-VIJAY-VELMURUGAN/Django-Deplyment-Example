from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context_dict = {'text':'hello world','number':100}
    return render(request,'basic_app/index.html',context = context_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')

def basic_app_home_page(request):
    return HttpResponse("<h1> Go to relative/ or other/</h1>")
