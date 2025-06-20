# Author: Daehwan Yeo 19448288
# Purpose: For WAF Assignment
# Reference: Lec 2, 3 slides, Lab 2, 3
# Last mod: 20/03/2025

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.category_tasks, name='category_tasks'),
]