def gcd(a,b):
    n1 = a
    n2 = b
    while(n2 > 0):
        q = n1 // n2
        r = n1 - q*n2
        n1 = n2
        n2 = r
    return n1

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("gcd of", x, "and", y, "is", gcd(x,y))


