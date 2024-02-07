from asyncio.windows_events import NULL
import email
import http
from django.http import HttpResponse
from django.shortcuts import redirect, render
from urllib import request
from django.shortcuts import render

from utilities.readyValues import ReadyFundPriories
from .forms import ProfileForm
from .models import Profile
# Create your views here.
def index(request):
    if request.method=="POST":
        request_data=ProfileForm(request.POST)
        
        if request_data.is_valid():
            if request_data.cleaned_data["email"]!=request_data.cleaned_data["Confirm_Email"]:
                return HttpResponse("<h1>Email not confirm<h1/>")
            if Profile.objects.filter(email=request_data.cleaned_data["email"]).exists():
                return HttpResponse("<h1> User with this email already exists<h1/>")   
            else :    
                
                request_data.save()                
                return redirect("done")
                
        else: 
            return HttpResponse("<h1>Invalid data<h1/>")
    form=ProfileForm()
    return render(request, "index.html", {'form': form})

def done(request):
    return render(request,"done.html")

def datalist(request):
    context=Profile.objects.all();
   
    if len(context)!=0:
        return HttpResponse(' | '.join(user.First_name for user in context))
    return HttpResponse("Database is empty")
def clear_database(request):
    Profile.objects.all().delete()
    return HttpResponse("Database cleared successfully")