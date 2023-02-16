
import clrprint as clr
import random

list = ["red","yellow","blue"]

for i in range(1,99999):        
    x = random.choice(list)
    clr.clrprint("\u2764 \u2133",clr=x,end=" ")
