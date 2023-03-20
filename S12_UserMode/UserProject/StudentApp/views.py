from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'home.html')

def sum(vaibhav):
    num1 = int(vaibhav.GET.get('n1'))
    num2 = int(vaibhav.GET.get('n2'))
    num3 = num1+num2
    print(num1,num2)
    return render(vaibhav,'result.html',{'x':num1,'y':num2,'z':num3})