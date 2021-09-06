from django.urls import path
from posts import views
urlpatterns = [
    path('',views.index,name='index'),
    path('post/<str:pk>',views.Post,name='Post')
]
 