

class Student:
    def __init__(self):
        print("i am created...",self)

    def display(self):
        print("hiii")
    
    def __del__(self):
        print("i am deleted...")

s = Student()
s.display()

del s

for i in range(100):
    print(i,end=" ")