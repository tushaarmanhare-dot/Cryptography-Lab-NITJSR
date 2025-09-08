#Finding Plaintext and Key in Affine cipher 
def mod_inverse(a, m):
    n1, n2 = m, a
    t1, t2 = 0, 1
    while n2 != 0:
        q = n1 // n2
        n1, n2 = n2, n1 - q * n2
        t1, t2 = t2, t1 - q * t2

    if n1 != 1:
        return None
    return t1 % m

def affine_encrypt(text, a, b, m=26):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            x = (((a * (ord(char) - base)) + b) % m)
            result += chr(x + base)
        else:
            result += char
    return result

def affine_decrypt(text, a, b, m=26):
    inv = mod_inverse(a, m)
    if inv is None:
        return None
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            x = ((((ord(char) - base) - b) * inv) % m)
            result += chr(x + base)
        else:
            result += char
    return result

# --- Extra predefined ciphertext brute-force ---
ctext = "WVZCPSCFZQCUUIMC"
print(f"\nPredefined Ciphertext: {ctext}\n")
print("Trying all possible (a, b) keys:\n")

# valid 'a' values must be coprime with 26
valid_a = []
for x in range(1, 26):
    if mod_inverse(x, 26) is not None:
        valid_a.append(x)
        
for a in valid_a:
    for b in range(26):
        pt = affine_decrypt(ctext, a, b)
        if pt:  # skip invalid a
            print(f"a={a:2}, b={b:2} -> {pt}")
