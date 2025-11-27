# YAK Authenticated Key Exchange Protocol (Simplified, Corrected)

def power_mod(base, exp, mod):
    """Efficient modular exponentiation"""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

# Step 1: Public parameters
p = int(input("Enter a large prime number (p): "))
g = int(input("Enter primitive root modulo p (g): "))

# Step 2: Long-term private/public keys
a_priv = int(input("Enter Alice's private key (a): "))
b_priv = int(input("Enter Bob's private key (b): "))

A_pub = power_mod(g, a_priv, p)
B_pub = power_mod(g, b_priv, p)

print("\nPublic keys:")
print("Alice's Public Key (A_pub):", A_pub)
print("Bob's Public Key (B_pub):", B_pub)

# Step 3: Ephemeral keys (temporary for each session)
x = int(input("\nEnter Alice's ephemeral private key (x): "))
y = int(input("Enter Bob's ephemeral private key (y): "))

X = power_mod(g, x, p)
Y = power_mod(g, y, p)

print("\nEphemeral public keys exchanged:")
print("Alice sends X =", X)
print("Bob sends Y =", Y)

# Step 4: Compute shared session key (authenticated)
# Correct session key computation
alice_key = power_mod(power_mod(Y, a_priv, p), x, p)
bob_key   = power_mod(power_mod(X, b_priv, p), y, p)

print("\nAlice's computed session key:", alice_key)
print("Bob's computed session key:", bob_key)

if alice_key == bob_key:
    print("\nAuthenticated Key Exchange Successful!")
    print("Shared Secret Key:", alice_key)
else:
    print("\nKey Mismatch! Authentication failed.")
