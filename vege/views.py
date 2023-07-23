# vege/views.py
from django.shortcuts import render

def recipes(request):
    # Your view logic here
    return render(request, 'vege/recipes.html')
