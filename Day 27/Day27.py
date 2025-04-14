# Day 27: CRUD with Django

# This is a summary-style walkthrough. Full Django project involves many files.
# 1. Create a Django project:
#    django-admin startproject mysite
# 2. Create an app:
#    cd mysite
#    python manage.py startapp myapp

# 3. Define a model in myapp/models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# 4. Register the model in myapp/admin.py
from django.contrib import admin
from .models import Task

admin.site.register(Task)

# 5. Add the app to settings.py -> INSTALLED_APPS = ['myapp', ...]

# 6. Create and apply migrations:
#    python manage.py makemigrations
#    python manage.py migrate

# 7. Create views and URLs in myapp/views.py and myapp/urls.py
from django.shortcuts import render, redirect
from .models import Task

# Views

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'add_task.html')

# 8. Configure URLs
# in mysite/urls.py -> path('tasks/', include('myapp.urls'))
# in myapp/urls.py -> path('', task_list, name='task_list'), path('add/', add_task, name='add_task')

# 9. Create templates: task_list.html and add_task.html in myapp/templates/

# Exercises:
# 1. Add a delete function for tasks.
# 2. Add an edit (update) function.
# 3. Style the templates using Bootstrap.
