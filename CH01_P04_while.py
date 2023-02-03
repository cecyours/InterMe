import os

sum = 0

while sum<=100:
    x = int(input("Enter the number : "))
    os.system('cls')
    sum = sum+x
    print("sum : ",sum)
    
print("final sum : ",sum)