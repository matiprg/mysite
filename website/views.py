from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse('<h1>Hi Welcome my website  </h1>')

def about_view(request):
    return HttpResponse({'<h1>About us  </h1>'})

def contact_view(request):
    return HttpResponse({'<h1>Contact us  </h1>'})
