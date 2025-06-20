# Author: Daehwan Yeo 19448288
# Purpose: For WAF Assignment, models
# Reference: Lec 2 slides, Lab 2
# Last mod: 19/03/2025

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField(blank=True, null=True)  # Optional text field

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='tasks')
    # In Lecture 3, Sheik emphasized that users can delete tasks but cannot delete categories

    def __str__(self):
        return self.title
