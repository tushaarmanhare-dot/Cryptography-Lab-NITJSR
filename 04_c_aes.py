# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# from Crypto.Util.Padding import pad, unpad

# # Generate a random 32-byte key (AES-256)
# key = get_random_bytes(32)

# # Generate a random 16-byte IV (AES block size = 16)
# iv = get_random_bytes(16)

# # Create AES cipher object for encryption
# cipher_encrypt = AES.new(key, AES.MODE_CBC, iv)

# # Message to encrypt
# plaintext = b"This is a test message for AES!"

# # Pad plaintext to match block size (16 bytes)
# padded_text = pad(plaintext, AES.block_size)

# # Encrypt
# ciphertext = cipher_encrypt.encrypt(padded_text)
# print("Ciphertext:", ciphertext)

# # Create AES cipher object for decryption (must use same key and IV)
# cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)

# # Decrypt and unpad
# decrypted_padded = cipher_decrypt.decrypt(ciphertext)
# decrypted_text = unpad(decrypted_padded, AES.block_size)

# print("Decrypted:", decrypted_text.decode())

# Advance Encryption Standard (AES)
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

def pad(data):
    block_size = AES.block_size
    padding = block_size - (len(data) % block_size)
    return data + bytes([padding] * padding)

def unpad(data):
    padding = data[-1]
    return data[:-padding]

def aes_encrypt(key, data):
    cipher = AES.new(key, AES.MODE_CBC)
    padded_data = pad(data)
    encrypted_data = cipher.encrypt(padded_data)
    return cipher.iv + encrypted_data

def aes_decrypt(key, encrypted_data):
    iv = encrypted_data[:AES.block_size]
    data = encrypted_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_data = cipher.decrypt(data)
    unpadded_data = unpad(decrypted_data)
    return unpadded_data

if __name__ == "__main__":
    flag = True
    while(flag):
        key_size = input("Input Key Size (16, 24 and 32): ")
        try:
            key_size = int(key_size)
        except:
            print("Error: Only Integers are supported.")
            continue

        if key_size == 16 or key_size == 24 or key_size == 32:
            flag = False
        else:
            print("Error: Supported Key Size are 16, 24 and 32 only.")

    key = get_random_bytes(key_size)

    data = b"Hello, AES!"

    encrypted_data = aes_encrypt(key, data)

    decrypted_data = aes_decrypt(key, encrypted_data)

    print("Plaintext:", data, "\n")
    print("Key:", key, "\n")
    print("Encryption:")
    print("Ciphertext:", encrypted_data, "\n")
    print("Decryption:")
    print("Plaintext:", decrypted_data)