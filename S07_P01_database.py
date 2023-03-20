
import pymysql as sql

import S07_P01_StudentModel as student
import names
from random import *

subject = ["Python","Html","JavaScript","Js","Java","C++","C","PHP","Ruby","Kotlin","Dart"]


con = sql.connect(user='root',password='',host='127.0.0.1',database='test')

cursor = con.cursor();

try:
    s = """CREATE TABLE Student_record(rollNo int(3) AUTO_INCREMENT PRIMARY KEY, name varchar(30),subject varchar(30),marks float(5))"""
    cursor.execute(s)
    con.commit()
except:
    pass

for i in range(1000):
    name = names.get_full_name()
    sub = choice(subject)
    marks = randint(99,500)
    print(name,sub,marks)
    s = "INSERT INTO `student_record`(`name`, `subject`, `marks`) VALUES ('{}','{}',{})"
    cursor.execute(s.format(name,sub,marks))
    con.commit()
print("Hows about that..")