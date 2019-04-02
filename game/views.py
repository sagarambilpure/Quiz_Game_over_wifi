from django.http import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render, redirect
import time
# Create your views here.
def home(request):
    return render(request,'game/home.html',{'gamingname' : request.user.gamingname })

def question(request):
    return render(request,'game/question.html',{'gamingname' : request.user.gamingname })

def index(request):
    return render(request,'game/index.html')

def register(request):
    return render(request, 'game/register.html', {})

def my_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        gamingname = user.gamingname
        return redirect('/question')
        # return HttpResponseRedirect(reverse("home",args=(username,)))
        # return render(request, 'game/home.html', {'gamingname' : user.gamingname})
    else:
        return render(request, 'game/index.html', {'loginfail' : True })

def answersubmit(request):
    question = request.POST['question']
    answer = 1
    gamingname = request.user.gamingname
    print("\n\n\n\n\n",question,gamingname,answer)
    a=Answer(uid=request.user,question_number=question,selected_answer=answer,time=time.time())
    a.save()
    return redirect('/home',{'gamingname' : gamingname})

def log_me_out(request):
    logout(request)
    return render(request, "game/index.html", {})

def signup(request):
    username = request.POST['username']
    password = request.POST['password']
    gamingname = request.POST['gamingname']
    user = UserOfApp.objects.create_user(username=username, password=password,gamingname=gamingname)

    user.save()
    return render(request, 'game/index.html',{'registered' : True})
