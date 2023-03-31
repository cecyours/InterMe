from django.shortcuts import render,redirect
from . forms import UserCreateForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required(login_url="sign-in-user")
def index(request): 
   return render(request,'index.html')


def signup_user(request):
   if request.user.is_authenticated:
         return redirect('index')
   userForm = UserCreateForm()

   if request.method == "POST":
      userForm = UserCreateForm(request.POST)
      if userForm.is_valid():
         userForm.save()
         print("data saved...")

      print("Hiii..")
   return render(request,'signup.html',{'userForm':userForm})
   pass

def logout_(request):
    logout(request)
    return redirect('sign-in-user')
    pass

def signin_user(request):
   if request.user.is_authenticated:
         return redirect('index')
   print("user : ",request.user)
   if request.method=="POST":
      username = request.POST.get('username')
      password = request.POST.get('password')
      print(username,password)
      user = authenticate(username=username,password=password)

      if user is not None:
         login(request,user)
         print("welcome")
         return redirect('index')
      else:
         print("invalid username/pass")
         

      # check redirect to home page.
   
   return render(request,'signin.html')
   pass
   pass

