from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

# Key generation
private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

message = b"hello world"

# Sign
signature = private_key.sign(message, hashes.SHA256())

# Verify
public_key.verify(signature, message, hashes.SHA256())

print("DSA signature OK")
