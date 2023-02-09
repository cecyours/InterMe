
def display():
    print("Hello There...")


def isPrime(num):

    for i in range(2,num//2):
        if num%2==0:
            return False
    return True
    


if __name__=="__main__":
    display()
