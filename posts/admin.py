from django.contrib import admin 
from posts.models import posts
# Register your models here.
#superuser:
    #name= admin
    #password= abhinav
admin.site.register(posts)  #this will show your model on admin panel