from django.shortcuts import render
from django.http import HttpResponse
import time
import .models import PageCount

# Create your views here.



def index(request):
    row, create = PageCount.objects.get_or_create(page='index')
    row.count += 1
    row.save()
    
    return HttpResponse("Hello, visitor #" +str(row.count) + ". You visited this page @ " time.strftime("%c"))