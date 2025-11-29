from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Key generation
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

message = b"hello world"

# Sign
signature = private_key.sign(
    message,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# Verify
public_key.verify(
    signature,
    message,
    padding.PKCS1v15(),
    hashes.SHA256()
)

print("RSA signature OK")
