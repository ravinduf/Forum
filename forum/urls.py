from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index,name="home_page"),
    path('question/<int:pk>', views.question_info ,name = "question_details"),
    path('addVote/<int:pk>', views.addVote, name = "addVote"),
    path('subVote/<int:pk>', views.subVote, name = "subVote"),

    
]