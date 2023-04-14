from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login

from .forms import SignupForm
# Create your views here.

def index(request):
    return render(request,'index.html')


def login1(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user.is_authenticated:
            # redict to home page..
            login(request,user)
            return render(request,'index.html')

    return render(request,'login.html')

def signup(request):
    sform = SignupForm(request.POST or None)

    if request.method=="POST":
        if sform.is_valid():
            sform.save()
            # redirect to login
            return redirect('my-login')
    return render(request,'signup.html',{'sform':sform})