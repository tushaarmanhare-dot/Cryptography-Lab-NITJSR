#RSA Implementation
def gcd(a,b):
    # Euclidean algorithm
    n1, n2 = a, b
    while(n2 > 0):
        q = n1 // n2
        n1, n2 = n2, n1 - q*n2
    return n1

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

def modinv(a, m):
    g, x, y = extgcd(a, m)
    if g != 1:
        print("Modular inverse does not exist for", a, "mod", m)
        return None
    else:
        return x % m

def enc(m, e, n):
    # encryption: c = m^e mod n
    return pow(m, e, n)

def dec(c, d, n):
    # decryption: m = c^d mod n
    return pow(c, d, n)

# Main program
p = int(input("Enter the first prime number: "))
q = int(input("Enter the second prime number: "))

n = p * q
phi = (p - 1) * (q - 1)

# Choose e (public exponent)
e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

# Compute d (private key exponent)
d = modinv(e, phi)

print("Public key: (e =", e, ", n =", n, ")")
print("Private key: (d =", d, ", n =", n, ")")

m = int(input("Enter the message (as a number < n): "))

# Encryption
c = enc(m, e, n)
print("Encrypted message:", c)

# Decryption
m_dec = dec(c, d, n)
print("Decrypted message:", m_dec)

