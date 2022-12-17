from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

# def hello_world(request):
#     return HttpResponse("Hello world!")
class HelloWorldView(View):
    def get(self, *args):
        return HttpResponse("Hello world!")

def check_kwargs(request, **kwargs):
    return HttpResponse(f"kwargs:<br>{kwargs}")