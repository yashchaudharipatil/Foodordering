from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples=[{'Name' :'yash' , 'Age':24},
           {'Name' :'yas' , 'Age':23} ]
    return render(request, "home/index.html", context={'peoples': peoples})
