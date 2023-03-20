from django.shortcuts import render
from . import demo
# Create your views here.
 
def page(request):
    print("Hello Me")
    x = "kites"
    return render(request,'index.html',{'name':x})

# Learn @ First 
def index(request):
    # list
    p1 = demo.Product("Car",499,"Be member and upload youopyright HD png image! Including transparent png clip art, cartoon, icon, logo, silhouette, watercolors, outlines, etc.",4,"img1.png")
    p2 = demo.Product("Bike",599,"Be member and upload your own & no-copyrigh transparent png clip art, cartoon, icon, logo, silhouette, watercolors, outlines, etc.",3,"img2.png")
    p3 = demo.Product("Cycle",799,"Be member and upload your own & noht HD png image! Including transparent png clip art, cartoon, icon, logo, silhouette, watercolors, outlines, etc.",5,"img3.png")
    
    list = [p1,p2]

    return render(request,'home.html',{'data':list})