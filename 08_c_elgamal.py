# ElGamal Cryptosystem Implementation
# No external libraries, works for small demo primes

def power_mod(a, b, p):
    """Efficient modular exponentiation"""
    result = 1
    a = a % p
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % p
        b //= 2
        a = (a * a) % p
    return result

# Step 1: Public parameters
p = int(input("Enter a large prime number p: "))
g = int(input("Enter primitive root modulo p (g): "))

# Step 2: Private and Public keys
x = int(input("Enter private key (x): "))  # secret
y = power_mod(g, x, p)                     # public key
print("\nPublic key (y, g, p):", (y, g, p))
print("Private key (x):", x)

# Step 3: Encryption
m = int(input("\nEnter message (as number < p): "))
k = int(input("Enter random key (k): "))   # ephemeral key

a = power_mod(g, k, p)
b = (m * power_mod(y, k, p)) % p
print("\nCiphertext (a, b):", (a, b))

# Step 4: Decryption
s = power_mod(a, x, p)
s_inv = pow(s, -1, p)   # modular inverse using pow in Python 3.8+
decrypted = (b * s_inv) % p
print("Decrypted message:", decrypted)