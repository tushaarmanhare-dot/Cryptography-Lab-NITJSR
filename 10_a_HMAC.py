import hashlib
from typing import Union

def _to_bytes(x: Union[str, bytes]) -> bytes:
    return x.encode() if isinstance(x, str) else x

def hmac_digest(key: Union[str, bytes],
                msg: Union[str, bytes],
                hash_name: str = "sha256") -> str:
    key = _to_bytes(key)
    msg = _to_bytes(msg)
    hash_ctor = lambda data=b'': hashlib.new(hash_name, data)
    block_size = hash_ctor().block_size

    # Keys longer than block_size are hashed first
    if len(key) > block_size:
        key = hash_ctor(key).digest()
    # Pad key to block_size
    key = key.ljust(block_size, b'\x00')

    o_key_pad = bytes((b ^ 0x5C) for b in key)
    i_key_pad = bytes((b ^ 0x36) for b in key)

    inner = hash_ctor(i_key_pad + msg).digest()
    outer = hash_ctor(o_key_pad + inner).hexdigest()
    return outer

# Example
if __name__ == "__main__":
    print(hmac_digest("secret", "message", "sha256"))
