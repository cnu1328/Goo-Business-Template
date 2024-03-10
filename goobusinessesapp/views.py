from django.shortcuts import render, redirect, HttpResponse
from django.http import FileResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from goobusinessesapp.models import AllServices
from django.http import JsonResponse
import time

OurMainURL = "https://goobusines.com/"

global lastUpdatetime
lastUpdatetime = datetime.now()


############# 28th jan 2024 ################
deletExtraImagesRUNNINGstatus = True

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def referral(request):
    
    return render(request, 'referral.html')


