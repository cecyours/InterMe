from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'home.html')

def sum(vaibhav):
    num1 = int(vaibhav.GET.get('n1'))
    num2 = int(vaibhav.GET.get('n2'))
    a = num1 + num2
    m = num1 * num2
    s = num1 - num2 
    d = num1 / num2
    z=str(a)+" , "+str(m)+" , "+str(s)+" , "+str(d)
    print(num1,num2)
    return render(vaibhav,'result.html',{'z':z})