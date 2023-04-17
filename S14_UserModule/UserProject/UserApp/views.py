import requests
import json
from django.shortcuts import render, redirect
from . forms import UserCreateForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import carousel,PostWork

from django.contrib.auth.decorators import login_required

# @login_required(login_url="sign-in-user")


def index(request):

    list = [
        carousel("Python", "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule. Python is dynamically typed and garbage-collected", "python.png", "#Page1"),
        carousel("java", "Java is a high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible.", "Java.png", "#Page1"),
        carousel("Spring Boot", "Spring Boot is an open source Java-based framework used to create a micro Service. It is developed by Pivotal Team and is used to build stand-alone and production ready spring applications.", "spring.png", "#Page1"),


    ]
    # list = [1,2,3]
    return render(request, 'index.html', {'list': list})


def result(request):

    return render(request, 'result.html')

def demo(request):
    username = request.GET.get("name")
    return render(request,'demo.html',{'data':username})
def home(request):
    return render(request,'home.html')

def user_dashboard(request):
    return render(request,'dashboard.html')

def get_list(request):
    list = PostWork.objects.all()
    # for i in list:
    return render(request,"list.html",{"data":list})


    pass
def user_test(request):
    #  load all Q.

    r = requests.get("https://cecyours.org/api/sample.json")
    # print(type(str(r.json())))

    return render(request, 'test.html', {"data": r.json()})
    pass


def signup_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    userForm = UserCreateForm()

    if request.method == "POST":
        userForm = UserCreateForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            print("data saved...")
            # redirect to login..
            return redirect("sign-in-user")
        print("Hiii..")
    return render(request, 'signup.html', {'userForm': userForm})
    pass


def logout_(request):
    logout(request)
    return redirect('sign-in-user')
    pass


def signin_user(request):
    if request.user.is_authenticated:
        return redirect('index')

    # print("user : ",request.user)

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print("welcome")
            return redirect('index')
        else:
            print("invalid username/pass")

        # check redirect to home page.
    return render(request, 'signin.html')
    pass
    pass
