from django.shortcuts import render,redirect
from . models import *
from . forms import bookform

# Create your views here.

def home(request):
    b = {
        'dwnl': book.objects.all()
    }
    return render(request,'home.html',b) 

def upload(request): 
    form =bookform() 
    if (request.method=="POST"): 
        form =bookform(request.POST,request.FILES) 
        if form.is_valid(): 
            form.save()
            return redirect(home)
    return render(request,'files.html',{"form":form})  