from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

# Key generation (using commonly used curve)
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

message = b"hello world"

# Sign
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

# Verify
public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))

print("ECDSA signature OK")
