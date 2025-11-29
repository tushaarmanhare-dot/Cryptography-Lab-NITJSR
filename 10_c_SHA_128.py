import hashlib
import base64
from typing import Union

def sha128(data: Union[bytes, str], *, encoding="utf-8", alg: str = "sha256") -> bytes:
    """
    Compute a 128-bit digest by hashing with `alg` (default SHA-256)
    and truncating to the first 16 bytes (128 bits).

    Returns the raw 16-byte digest.
    """
    if isinstance(data, str):
        data = data.encode(encoding)
    h = hashlib.new(alg)
    h.update(data)
    full = h.digest()            # full digest (e.g. 32 bytes for SHA-256)
    return full[:16]             # truncate to 16 bytes (128 bits)

# helpers to return hex or base64 strings
def sha128_hex(data: Union[bytes, str], **kwargs) -> str:
    return sha128(data, **kwargs).hex()

def sha128_b64(data: Union[bytes, str], **kwargs) -> str:
    return base64.b64encode(sha128(data, **kwargs)).decode('ascii')


# Example usage
if __name__ == "__main__":
    s = "hello world"
    raw = sha128(s)            # bytes, 16 bytes long
    print("raw bytes:", raw)
    print("hex:", sha128_hex(s))
    print("base64:", sha128_b64(s))
