

# type cast

d = [9,5,3,4,1,6,8,6]

print(d)

s = set(d) # list - > set

new_data = list(s)

print(s,new_data[::-1])

l = []
l = list()

for i in range(len(new_data)-1,0,-1):
    l.append(new_data[i])

print(l)


