from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

"""rooms=[
    {'id':1,'name':'Lets learn python'},
    {'id':2,'name':'Lets learn Django'},
    {'id':3,'name':'Frontend Developer'},
    {'id':4,'name':'Backedn Developer'}

]"""

def home(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    room=Room.objects.get(id=pk)
    context={'room':room}
    return render(request,'base/room.html',context)

# Create your views here.
