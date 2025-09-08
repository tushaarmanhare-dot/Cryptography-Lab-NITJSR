#Finding Plaintext and Key in Multiplicative cipher 
from math import gcd

def mod_inverse(a, m=26):
    for x in range(1,m):
        if(a * x) % m == 1:
            print("Inv key: ",x)
            return x
    return None
    
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

ctext = "UWEEWGNMGUZBYXY"
print(f"Ciphertext: {ctext}\n")
for key in range(26):
    text = decrypt(ctext,key)

    print(f"Key {key:2} -> {text}")
