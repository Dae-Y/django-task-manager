# Author: Daehwan Yeo 19448288
# Purpose: For WAF Assignment
# Reference: Lec 2 slides, Lab 2
# Last mod: 20/03/2025

from django.contrib import admin
from .models import Task, Category

admin.site.register(Task)
admin.site.register(Category)
