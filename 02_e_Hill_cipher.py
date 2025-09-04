#Implement Hill Cipher
import numpy as np

def char_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_char(n):
    return chr((n % 26) + ord('A'))

def clean_text(text,size):
    cleaned = ''
    for c in text:
        if c.isalpha():
            cleaned += c.upper()
    text = cleaned
    if len(text) % size != 0:
        text += 'X' * (size - len(text) % size)
    return text

def hill_encrypt(plaintext,key_matrix):
    size = key_matrix.shape[0]
    plaintext = clean_text(plaintext,size)

    ciphertext = ""
    for i in range(0,len(plaintext),size):
        block = []
        for c in plaintext[i:i+size]:
            block.append(char_to_num(c))
        block_vec = np.array(block).reshape(-1,1)
        cipher_vec = np.dot(key_matrix,block_vec) % 26
        for n in cipher_vec.flatten():
            ciphertext += num_to_char(int(n))
    return ciphertext

def mod_inverse(a, m=26):
    for x in range(1,m):
        if(a * x) % m == 1:
            return x
    return None

def hill_decrypt(ciphertext,key_matrix):
    size = key_matrix.shape[0]

    det = int(round(np.linalg.det(key_matrix))) % 26
    inv_det = mod_inverse(det,26)
    if inv_det is None:
        return "Key matrix is not invertible modulo 26"
    
    adj = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inv_matrix = (inv_det * adj) % 26

    plaintext = ""
    for i in range(0,len(ciphertext),size):
        block = []
        for c in ciphertext[i:i+size]:
            block.append(char_to_num(c))
        block_vec = np.array(block).reshape(-1,1)
        plain_vec = np.dot(inv_matrix,block_vec) % 26
        for n in plain_vec.flatten():
            plaintext += num_to_char(n)
    return plaintext.rstrip('X')

key = np.array([[3,3],
                [2,5]])

msg = input("Enter message:")
enc = hill_encrypt(msg,key)
dec = hill_decrypt(enc,key)

print("Original message: ",msg)
print("Encrypted message: ",enc)
print("Decrypted message: ",dec)
