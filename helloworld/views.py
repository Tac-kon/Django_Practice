from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse('Hello World!')
