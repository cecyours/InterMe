

def isPrime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False    
    return True
        

def displayFactors(num):
    for i in range(2,num+1):
        f = isPrime(i)
        if f:
            while num%i==0:
                num = num//i;
                print(i,end=" ")


# 38

# 2x19x1

# 40
#2x2x2x5

