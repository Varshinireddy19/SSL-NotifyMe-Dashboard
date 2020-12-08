from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from pyfcm import FCMNotification
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import RegisterForm
# Create your views here.


def register(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()
	    return redirect("/index")
    else:
	    form = RegisterForm()

    return render(response, "main/register.html", {"form":form})




def index(request):
   # if request.user.is_authenticated:
    return render(request, 'main/index.html')
  


def sendnotification(request):
    if request.method == 'POST':
        push_service = FCMNotification(api_key='AAAAlEVrg54:APA91bGrlZhOQrIRZgkvteLycBjCJEMVZB5lD3jYna9VM_BQ6B_Sj9I7Y5MWGq_9swsY6m0654TxWaYPHLfi3Ea5SkBs412uSxvt5r-M3UiTZQxIAgRJZ7O-d3Y_sWRNW012eFK4jED8')
        registration_id1 = 'eU75fuaIRmyAVcBuuh0csV:APA91bHtG1RK8JwRrQQ85RESwF7n6Ra42LxRiKJtI0XeJnZFvxunStBzUNQMIp1b4BuNZu0lnE9kE3s_--z9nSpRcU31io74-T4-HiVDrPPzfgYM6mA4LX-GvFK9NBIeiIjcyKcLxjGT'
       # registration_id2 = ""
        message_title = request.POST.get('title')
        message_body = request.POST.get('body')
        r1 = push_service.notify_single_device(registration_id=registration_id1, message_title=message_title, message_body=message_body)
      #  r2 = push_service.notify_single_device(registration_id=registration_id2, message_title=message_title, message_body=message_body)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'main/index.html')
def home(request):
    return render(request, 'main/base.html')        