
# s = "Hello {}, im {}"

# print(s.format("Barot","Work"))

# s = "Hello {name}, i am {person}"
# print(s.format(name='barot',person='ip'))

# s = "Hi {1}, i am {0}"
# print(s.format("Mohan","Raju"))


data = {

    '102':{
        'name':'rio',
        'subject':'python',
        'marks':923.34
    },

    '103':{
        'name':'rio',
        'subject':'python',
        'marks':923.34
    },
    '105':{
        'name':'rio',
        'subject':'python',
        'marks':923.34
    },

    '108':{
        'name':'rio',
        'subject':'python',
        'marks':923.34
    },
    
}


print("%5s | %10s | %10s | %7s |"%("srNo","name","subject","marks"))
for i in data:
    print("%5s + %10s + %10s + %7s +"%("---","---","------","-----"))
    print("{:^5} | {:^10} | {:^10} | {:>7} |".format(i,data[i]["name"],data[i]["subject"],data[i]["marks"]))
