#Extended Euclidean Algorithm
def extgcd(a,b):
    n1, n2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while(n2 != 0):
        q = n1 // n2
        r = n1 - q*n2
        n1, n2 = n2, r

        s = s1 - q*s2
        s1, s2 = s2, s

        t = t1 - q*t2
        t1, t2 = t2, t
    return n1,s1,t1

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: " ))

g,s,t = extgcd(x,y)

print(f"gcd({x},{y}) = {g}")
print(f"Values of s and t are: s = {s}, t = {t}")
print(f"Verification: {x}*({s}) + {y}*({t}) = {g}")

