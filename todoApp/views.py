from django.shortcuts import render, redirect , get_object_or_404
from  django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.

def loginn(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pwd")

        # check if user exits
        user = User.objects.filter(username=username).exists()
        if not user:
            messages.error(request,"Username does not exist")
            return redirect('login')
        #authenticate
        user = authenticate(username= username, password=password)

        if user is None:
            messages.error(request,"Incorrect password")
            return redirect("login")
        else:
            login(request,user)
            return redirect("home")

        
    
    return render(request,"loginn.html")

def signup(request):
    # get info from form
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pwd")


    #check if user exits
        user = User.objects.filter(username=username)

        if user:
            messages.info(request,"User name already exists")
            return redirect('register')
        
        user = User.objects.create_user(
            username=username, email=email,password=password
        )

        user.save()
        messages.info(request,"Account created successfully")
        return redirect("login")

    #register user
    return render(request, "signup.html")

@login_required
def home(request):
    #read task
    all_tasks = Task.objects.all();
    context = {'tasks':all_tasks}

    return render(request, "index.html",context=context)

def log_out(request):
    logout(request)
    return redirect("login")




# create task
def add_task(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            user = request.user
            task = request.POST.get("task")
            Task.objects.create(user=user, name=task)
            return redirect('home')
    return redirect("home")

#delete a task

def remove_task(request,id):
    task = Task.objects.filter(task_id=id)
    task.delete()
    return redirect("home")

#update a task

def edit_task(request,id):
    task = Task.objects.get(task_id=id)
    
    context ={'name': task.name}
    if request.method == 'POST':
        task_name = request.POST.get("task")
        task.name= task_name
        task.save()
        return redirect("home")


    return render(request,"update.html", context=context)


    
