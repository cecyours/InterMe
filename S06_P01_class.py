<<<<<<< HEAD


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
=======


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
>>>>>>> 5f13f01fb3310c1cd630e84b82790a0e8749c085
    print(i,end=" ")