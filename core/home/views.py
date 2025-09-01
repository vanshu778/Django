from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples = [
        {'name':'Vanshika','age':26},
        {'name':'cutiee','age':12}
    ]
    
    return render(request,"home/index.html", context={'page':'Django Learning','peoples':peoples})

def about(request):
    context = {'page':'About'}
    return render(request,"home/about.html",context)

def contact(request):
    context = {'page':'Contact'}

    return render(request,"home/contact.html",context)

def success_page(request):
    return HttpResponse("<h1>Hey This is a success page.<h1>")
