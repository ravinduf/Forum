from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index,name="home_page"),
    path('question/<int:pk>', views.question_info ,name = "question_details"),
    path('addVote/<int:pk>', views.addVote, name = "addVote"),
    path('subVote/<int:pk>', views.subVote, name = "subVote"),
    path('addQuestion', views.addQuestion, name = "addQuestion"),
    path('questionDelete/<int:pk>', views.questionDelete, name = "questionDelete"),
    path('answerDelete/<int:pk>', views.answerDelete, name = "answerDelete"),
    path('addAnswerVote/<int:pk>', views.addAnswerVote, name = "addAnswerVote"),
    path('subAnswerVote/<int:pk>', views.subAnswerVote, name = "subAnswerVote"),
    path('editQuestion/<int:pk>', views.editQuestion, name = "editQuestion"),
    path('editAnswer/<int:pk>', views.editAnswer, name = "editAnswer"),
]