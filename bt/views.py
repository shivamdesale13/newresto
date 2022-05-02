from email import message
from django.shortcuts import render
from math import ceil
import json
from django.http import HttpResponse 
from .models import Contact,booking


# Create your views here.
def index(request):
    return render(request, 'bt/index.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, 'bt/index.html')