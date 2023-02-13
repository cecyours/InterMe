import S04_P02_import_pkg as me

me.display()

x = int(input("Enter a num : "))

f = me.isPrime(x)

if f:
    print("prime")
else:
    print("!prime")

