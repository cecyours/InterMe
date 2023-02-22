
import names
import random
import datetime
import pymysql
con = pymysql.connect(user='root',password='',host='127.0.0.1',database='test')
cursor = con.cursor()


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

    s = "INSERT INTO student_record(name,age,subject,marks,date) VALUE('{}',{},'{}',{},'{}')"
    cursor.execute(s.format(name,age,subject,marks,str(date)))
    con.commit()
