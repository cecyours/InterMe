from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')

def add(request):
    n1 = int(request.POST.get('n1'))
    n2 = int(request.POST.get('n2'))
    n3 = n1+n2
    return render(request,"add.html",{'num1':n1,'num2':n2,'num3':n3})