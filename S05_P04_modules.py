
class ListWork:
    # constructors
    def __init__(self):
        print("My Work List")

    #destructors
    def __del__(kartik):
        print("i am deleted...")
    
class StrWork:
    def __init__(self):
        print("My Work str...")


class Person:
    def __init__(self,personName):
        self.personName = personName
        print("welcome ",self.personName)
    
    def __del__(self):
        print(self.personName," is deleted..")