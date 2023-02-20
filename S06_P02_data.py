Cimport json

class Product:
    
    def __init__(self,emp_id,name,price,city):
        self.emp_id = emp_id
        self.name = name
        self.price = price
        self.city = city

product = list()

with open('./json_code.json') as file:
    data = json.load(file)
    for i in data:
        id = i['EmpNo']
        name = i['Product']
        price = i['Price']
        city = i['City']

        p = Product(id,name,price,city)
        product.append(p)


# for i in product:
#     print(i.name, i.city, i.emp_id, i.price)


pName = input("Enter product Name : ")

for i in product:
    if (i.name==pName):
        print(i.name, i.city, i.emp_id, i.price)
