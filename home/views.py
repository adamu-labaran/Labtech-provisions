# from django.http import HttpResponse
from django.shortcuts import render

# using template
def index(request):
    return render(request, template_name='index.html')



def about(request):
    return render(request, template_name='about.html')