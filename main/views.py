from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

# View for home path
def home(request):
    return render(request, template_name='main/home.html')

# View for registering the user
def register(request):
    # if get request
    if request.method == 'GET':
        return render(request, template_name='main/register.html', context={'form': UserCreationForm()})
    # if post request
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # creating user and saving
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('main:home')
            except IntegrityError:
                return render(request, template_name='main/register.html', context={'form': UserCreationForm(), 'error': 'Username already taken.'})
        else:
            return render(request, template_name='main/register.html', context={'form': UserCreationForm(), 'error': 'Passwords did not match.'})

# View for loging the user
def loginuser(request):
    # if get request
    if request.method == 'GET':
        return render(request, 'main/login.html', {'form': AuthenticationForm()})
    # if post request
    else:
        # authenticating the user
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, template_name='main/login.html', context={'form': AuthenticationForm(), 'error': 'Username and password not matched.'})
        else:
            login(request, user)
            return redirect("main:home")

# View for log out the user
@login_required
def logoutuser(request):
    logout(request)
    return redirect('main:home')

# View for fetching the all tasks for a user
@login_required
def currenttasks(request):
    # fetching all tasks
    tasks = Task.objects.filter(user=request.user).order_by('-date')
    # fetching tasks which are not completed
    non_complete_tasks = Task.objects.filter(user=request.user, completed=False)
    return render(request, template_name="main/tasks.html", context={'tasks': tasks, "count": non_complete_tasks.count})

# View for creating the task for a user
@login_required
def createtask(request):
    if request.method == 'GET':
        return render(request, template_name="main/create.html", context={'form': TaskForm()})
    else:
        try:
            # creating task and saving for a user
            form = TaskForm(request.POST)
            newtask = form.save(commit=False)
            newtask.user = request.user
            newtask.save()
            return redirect("main:currenttasks")
        except ValueError:
            return render(request, template_name="main/create.html", context={'form': TaskForm(), 'error': "Bad data passed in."})

# View for marking a task completed
@login_required
def completetask(request, task_pk):
    # finding the task of an id
    task = get_object_or_404(Task, pk=task_pk, user=request.user)
    task.completed = True
    task.save()
    return redirect("main:currenttasks")
    
# View for deleting a task
@login_required
def deletetask(request, task_pk):
    # finding the task of an id
    task = get_object_or_404(Task, pk=task_pk, user=request.user)
    task.delete()
    return redirect("main:currenttasks")
    

