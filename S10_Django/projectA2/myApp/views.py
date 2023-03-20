from django.shortcuts import render

# Create your views here.

from . import cartoon
def index(request):
    c1 = cartoon.cartoon('BEN 10',5,'img1.png', 'Ben 10 is an American media franchise created by Man of Action Studios, produced by Cartoon Network Studios and owned by Warner Bros. Discovery.')
    c2 = cartoon.cartoon('Doremon',3,'img2.png', 'Doraemon is a fictional character in the Japanese manga and animated series of the same name created by Fujiko F. Fujio. Doraemon is a male robotic earless cat that travels back in time from the 22nd century to aid a preteen boy named Nobita')
    c3 = cartoon.cartoon('Kick" Buttowski',5,'img3.png', 'Clarence Francis "Kick" Buttowski: a 10-year-old amateur, thrill-seeking often reckless daredevil. His main goal out of life is to embrace each day as if it')
    
    list = [c3,c1,c2,c3]
    return render(request,'index.html',{'data':list})