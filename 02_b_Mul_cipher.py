#Implement Affine Cipher
def mod_inverse(a,m):
    n1, n2 = m, a
    t1, t2 = 0, 1
    while n2 != 0:
        q = n1 // n2
        n1, n2 = n2, n1 - q*n2
        t1, t2 = t2, t1 - q*t2

    if n1 != 1:
            return None
    print("Inverse key: ",t1 % m)
    return t1 % m

def affine_encrypt(text,a,b,m=26):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            x = (((a * (ord(char) - base)) + b ) % m)
            result += chr(x + base)
        else:
            result += char
    return result

def affine_decrypt(text,a,b,m=26):
    inv = mod_inverse(a,m)
    if inv is None:
        return "Invalid key! It must be coprime with 26."
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            x = ((((ord(char) - base) - b) * inv ) % m)
            result += chr(x + base)
        else:
            result += char
    return result

msg = input("Enter the message: ")
a = int(input("Enter the multiplicative key: "))
b = int(input("Enter the additive key: "))

enc = affine_encrypt(msg,a,b)
dec = affine_decrypt(enc,a,b)

print("Original message:",msg)
print("Encrypted message:",enc)
print("Decrypted message:",dec)
          
