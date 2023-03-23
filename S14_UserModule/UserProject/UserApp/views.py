from django.shortcuts import render
from . forms import UserCreateForm
# Create your views here.

def index(request): 
   return render(request,'index.html')


def signup_user(request):
   userForm = UserCreateForm()
   return render(request,'signup.html',{'userForm':userForm})
   pass

def signin_user(request):
   
   return render(request,'signin.html')
   pass
   pass

