from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from App.forms import TODOForm, TasksForm
from App.models import TaskMan, Action
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TaskMan.objects.filter(user = user).order_by('priority')
        return render(request , 'index.html' , context={'form' : form , 'todos' : todos})

def login(request):
    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            "form" : form1
        }
        return render(request , 'login.html' , context=context )
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user)
                return redirect('home')
        else:
            context = {
                "form" : form
            }
            return render(request , 'login.html' , context=context )


def signup(request):

    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request , 'signup.html' , context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)  
        context = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request , 'signup.html' , context=context)



@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print("",user)
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            Action.objects.create(user=request.user, task=0)
            print(todo)
            return redirect("home")
        else: 
            return render(request , 'index.html' , context={'form' : form})


def delete_todo(request , id ):
    print(id)
    TaskMan.objects.get(pk = id).delete()
    Action.objects.create(user=request.user, task=2)

    return redirect('home')

def change_todo(request , id  , status):
    print("####", request)
    todo = TaskMan.objects.get(pk = id)
    todo.status = status
    todo.save()
    Action.objects.create(user=request.user, task=1)
    return redirect('home')


def signout(request):
    logout(request)
    return redirect('login')



#@Action 
def activity_log(request):
    ctx={} 
 
    tm = list(Action.objects.filter(user=request.user).values("task","user__username"))
    print("tm",tm)

    count = 0
    print(tm[0])
    for i in tm:
        print(i['task'])
        # exit('stop')
        if i['task'] == 2:
            tm[count]['task'] = "Delete"

        elif i['task']== 1:
            tm[count]['task'] = "Update"
        
        else:
            tm[count]['task'] = "Create"
    
        count+=1
    """
    
    for x in T:
        print(x.user)
        print(x.action_task)
    """
    ctx['action_feed']=tm
    #ctx1['user'] = T
    # return None
    return render(request,'activity.html',ctx)






