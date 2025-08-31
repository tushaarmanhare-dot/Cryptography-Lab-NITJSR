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

msg = input("Enter the message: ")
key = int(input("Enter the value of key: "))

encrypted = caesar_encrypt(msg,key)
decrypted = caesar_decrypt(encrypted,key)

print("Original message:",msg)
print("Encrypted message:",encrypted)
print("Decrypted message:",decrypted)
          
                
