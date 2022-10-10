from django.contrib import admin
from django.urls import path, include
from question_result import views

urlpatterns = [
    path('', views.question, name = 'question_result'),    
]