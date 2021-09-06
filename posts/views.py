from django.shortcuts import render 
from .models import posts
# Create your views here.
def index(request):
    post= posts.objects.all()   #this will give a list of all the objecs we've made in our model
    return render(request,'index.html',{'posts':post})


def Post(request,pk):   #this is dynamic url routing
    post_expanded= posts.objects.get(id= pk)     #this will help to get the post from database with id= pk
    #here ID is used because we know that when we create a model, django atuomatically gives an ID to every object

    return render(request,'posts.html',{'posts':post_expanded}) 