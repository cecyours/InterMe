
import S07_P01_StudentModel as student
import names
from random import *

subject = ["Python","Html","JavaScript","Js","Java","C++","C","PHP","Ruby","Kotlin","Dart"]

for i in range(10):
    name = names.get_full_name()
    sub = choice(subject)
    marks = randint(99,500)
    print(name,sub,marks)