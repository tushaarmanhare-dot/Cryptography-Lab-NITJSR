#Finding Plaintext and Key in Caesar cipher 
def caesar_encrypt(text,shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text,shift):
    return caesar_encrypt(text,-shift)

ctext = "MKTGLFBMHKWXKLGHP"
print(f"Ciphertext: {ctext}\n")
for key in range(26):
    text = caesar_decrypt(ctext,key)
    print(f"Key {key:2} -> {text}")
   