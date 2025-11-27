# Diffie-Hellman Key Exchange
import random
from Crypto.Util import number
from Crypto import Random

def generatePublicKey():
    bits = 10
    g = 2
    n = number.getPrime(bits, randfunc=Random.get_random_bytes)
    return n, g

def generatePrivateKey():
    alice = random.randint(0, 100)
    bob = random.randint(0, 100)

    while alice == bob:
        alice = random.randint(0, 100)
        bob = random.randint(0, 100)
    
    return alice, bob

def calculatePassingKey(g, private_key, n):
    return pow(g, private_key, n)

def calculateSharedKey(passing_key, private_key, n):
    return pow(passing_key, private_key, n)

if __name__ == "__main__":
    n, g = generatePublicKey()
    private_key_alice, private_key_bob = generatePrivateKey()

    passing_key_alice = calculatePassingKey(g, private_key_alice, n)
    passing_key_bob = calculatePassingKey(g, private_key_bob, n)

    shared_key_alice = calculateSharedKey(passing_key_bob, private_key_alice, n)
    shared_key_bob = calculateSharedKey(passing_key_alice, private_key_bob, n)

    print("n:\t\t\t", n)
    print("g:\t\t\t", g)
    
    print("\nAlice -> Private Key:\t", private_key_alice)
    print("Bob -> Private Key:\t", private_key_bob)
    
    print("\nAlice -> Passing Key:\t", passing_key_alice)
    print("Bob -> Passing Key:\t", passing_key_bob)

    print("\nBob -> Alice:\t\t", passing_key_bob)
    print("Alice -> Bob:\t\t", passing_key_alice)

    print("\nAlice -> Shared Key:\t", shared_key_alice)
    print("Bob -> Shared Key:\t", shared_key_bob)
