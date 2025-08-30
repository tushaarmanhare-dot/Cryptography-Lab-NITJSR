def mod_inverse(a,p):
    n1, n2 = p, a
    t1, t2 = 0, 1

    while n2 != 0:
        q = n1 // n2
        n1, n2 = n2, n1 - q*n2
        t1, t2 = t2, t1 - q*t2

    if n1 != 1:
        return None  #inverse doesnt exist
    return t1 % p  #positive result

x = int(input("Enter the number: " ))
y = int(input("Enter prime number p: "))

mul_inv = mod_inverse(x,y)

print(f"In GF({y})")
if mul_inv:
    print(f"Multiplicative inverse of {x} is {mul_inv} (since {x} * {mul_inv} % {y} = 1)")
else:
    print(f"No multiplicative inverse exists for {x} in GF({y})")
    

