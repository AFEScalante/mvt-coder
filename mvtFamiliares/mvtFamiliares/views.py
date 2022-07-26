from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def hello_page(request):
    return render(request, 'hello.html', context={})