from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Generate a random 24-byte key (for 3DES)
key = DES3.adjust_key_parity(get_random_bytes(24))

# Generate a random 8-byte IV (block size for DES is 8)
iv = get_random_bytes(8)

# Create cipher object for encryption
cipher_encrypt = DES3.new(key, DES3.MODE_CBC, iv)

# Message to encrypt
plaintext = b"Hello, this is a 3DES test!"
print("Plaintext:",plaintext)

# Pad plaintext to match block size
padded_text = pad(plaintext, DES3.block_size)

# Encrypt
ciphertext = cipher_encrypt.encrypt(padded_text)
print("Ciphertext:", ciphertext)

# Create cipher object for decryption (must use same key and IV)
cipher_decrypt = DES3.new(key, DES3.MODE_CBC, iv)

# Decrypt and unpad
decrypted_padded = cipher_decrypt.decrypt(ciphertext)
decrypted_text = unpad(decrypted_padded, DES3.block_size)

print("Decrypted:", decrypted_text.decode())