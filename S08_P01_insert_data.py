
import names
import random
import datetime
import pymysql
# con = pymysql.connect(user='root',password='',host='127.0.0.1',database='test')
# cursor = con.cursor()


sub_list = ["python","Java","php","DS","C++"]

for i in range(100):
    name = names.get_full_name()
    age = random.randint(14,23)
    subject = random.choice(sub_list)
    marks = random.randint(300,500)
    mm = random.randint(1,12)
    dd = random.randint(1,20)
    yyyy = random.randint(2000,2023)
    date = datetime.date(yyyy,mm,dd)
    print("{:20} {:3} {:10} {:5} {}".format(name,age,subject,marks,str(date)))

    # s = "INSERT INTO student_record(name,age,subject,marks,date) VALUE('{}',{},'{}',{},'{}')"
    # cursor.execute(s.format(name,age,subject,marks,str(date)))
    # con.commit()
# -------------------------------
# import names 
# import random as r
# import pymysql
# import datetime

# con = pymysql.connect(user='root',password='',host='127.0.0.1',database='students')

# print("connection done..")

# data = dict()
# subject = ["python","java","C++","php","html","C","js"]

# cursor = con.cursor()
# # for i in range(600):
# #     name = names.get_full_name()
# #     sub = r.choice(subject)
# #     marks = r.randint(300,500)
# #     age = r.randint(12,23)
# #     mm = r.randint(1,12)
# #     dd = r.randint(1,20)
# #     yyyy = r.randint(2012,2023)
# #     date = datetime.date(yyyy,mm,dd)
# #     print(date)
# #     s = "INSERT INTO person(name,age,subject,marks,date) VALUES('{}',{},'{}',{},'{}')"
# #     cursor.execute(s.format(name,age,sub,marks,str(date)))
# #     con.commit()


# s = "SELECT * FROM person WHERE date > 2020-01-01"
# cursor.execute(s)
# x = cursor.fetchall()

# for i in x:
#     print("{:4} + {:20} + {:2} + {:7} + {:5} + {}".format("----","--------------------","--","------","----","------"))
#     print("{:4} | {:20} | {:2} | {:7} | {:5} | {}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
