

start = int(input("Enter the number "))
end = int(input("Enter the number "))

for i in range(1,11):
    for j in range(start,end+1):
        print(f"{j:2} X {i:2} = {j*i:2} ",end=" | ")
    print()

