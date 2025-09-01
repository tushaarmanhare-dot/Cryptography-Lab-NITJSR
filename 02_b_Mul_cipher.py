#Implement Multiplicative Cipher 
from math import gcd

def mod_inverse(a, m=26):
    for x in range(1,m):
        if(a * x) % m == 1:
            print("Inv key: ",x)
            return x
    return None

def encrypt(text,shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            result += chr(((ord(char) - base) * shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text,shift):
    inv = mod_inverse(shift)
    if inv is None:
        return "No inverse exists choose a different key!"
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            result += chr(((ord(char) - base) * inv) % 26 + base)
        else:
            result += char
    return result

msg = input("Enter the message: ")
key = int(input("Enter the key value(must be coprime with 26): "))

if gcd(key,26) != 1:
    print("Invalid key! It must be coprime with 26")
else:
    enc = encrypt(msg,key)
    dec = decrypt(enc,key)
    print("Original message:", msg)
    print("Encrypted message:", enc)
    print("Decrypted message:", dec)


