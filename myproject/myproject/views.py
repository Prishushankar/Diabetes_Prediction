#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
   # return HttpResponse('Hello I am the home page.')
   return render(request,'home.HTML')
def about(request):
   # return HttpResponse('I am the about page.')
    return render(request,'about.HTML')