# Author: Daehwan Yeo 19448288
# Purpose: For WAF Assignment, views
# Reference: Lec 2, 3 slides, Lab 2, 3
# Last mod: 20/03/2025

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Task, Category


# Task list view
def task_list(request):
    tasks = Task.objects.all()  # Get all tasks from the database
    return render(request, 'task_list.html', {'tasks': tasks})

# Task detail view
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)  # Get task by ID or 404 if not found
    return render(request, 'task_detail.html', {'task': task})

# Category list view
def category_list(request):
    categories = Category.objects.all()  # Get all categories
    return render(request, 'category_list.html', {'categories': categories})

# Category tasks view
def category_tasks(request, category_id):
    category = get_object_or_404(Category, pk=category_id)  # Get category by ID or 404
    tasks = category.tasks.all()
    return render(request, 'category_tasks.html', {'category': category, 'tasks': tasks})

# Home view
def home(request):
    return render(request, 'home.html')


# Error handling functions in lec 3 slides
def error_400(request, exception):
    return HttpResponse('Bad request.', status=400)
def error_403(request, exception):
    return HttpResponse('You do not have permission to view this page.', status=403)
def error_404(request, exception):
    return HttpResponse('Cannot find the content.', status=404)
def error_500(request):
    return HttpResponse('Internal Server Error.', status=500)
