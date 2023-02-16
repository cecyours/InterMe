# propties+action
# properties : variable (one word value)
# action : method process
class Dog:
    def __init__(me):
        me.name = "Tommy"
        me.breed = "Vodaphone wala kutta"
    
    def bark(x):
        print("my dog is barking... ",x.name,x.breed)

x = Dog()

x.bark();
