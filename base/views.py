from django.shortcuts import redirect

import requests as req

from django.http import JsonResponse,HttpResponse  

import random

from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

import json

import ast

# perform business logic
@csrf_exempt

def home(request):

    return redirect('Home.views.welcome')



@csrf_exempt

def welcome(request):

    return render(request,"home.html",{})

    # perform business logic

@csrf_exempt

def software_development(request):

    return render(request,"software_development.html",{})

@csrf_exempt

def research(request):

    return render(request,"research.html",{})

@csrf_exempt

def artistic(request):

    return render(request,"artistic.html",{})

@csrf_exempt  

def start(request):

    n = request.POST
    return JsonResponse({'sender_and_receiver_comparing_sample_equivalent':'response'})
