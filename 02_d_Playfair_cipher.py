#Implement Playfair Cipher
def gen_key_matrix(key):
    key = key.upper().replace("J","I")
    seen = set()
    matrix = []

    for char in key:
        if char.isalpha() and char not in seen:
            seen.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    
    rows = []
    for i in range(0,25,5):
        rows.append(matrix[i:i+5])
    return rows

def print_matrix(matrix):
    print("Playfair key matrix: ")
    for row in matrix:
        print(" ".join(row))
    print()

def find_pos(matrix,char):
    for i,row in enumerate(matrix):
        if char in row:
            return i,row.index(char)
    return None

def playfair_encrypt(text,matrix):
    text = text.upper().replace("J","I")
    clean_text = ""
    for c in text:
        if c.isalpha():
            clean_text += c
    text = clean_text

    digraphs =[]
    i = 0
    while i < len(text):
        a = text[i]
        b = ""
        if i+1 < len(text):
            b = text[i+1]
        if a == b:
            digraphs.append(a + "X")
            i += 1
        else:
            if b:
                digraphs.append(a + b)
                i += 2
            else:
                digraphs.append(a + "X")
                i += 1

    result = ""
    for pair in digraphs:
        r1,c1 = find_pos(matrix,pair[0])
        r2,c2 = find_pos(matrix,pair[1])

        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]

        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result

def playfair_decrypt(text,matrix):
    text = text.upper().replace("J","I")
    clean_text = ""
    for c in text:
        if c.isalpha():
            clean_text += c
    text = clean_text
    
    result = ""
    for i in range(0,len(text),2):
        a, b = text[i], text[i+1]
        r1, c1 = find_pos(matrix,a)
        r2, c2 = find_pos(matrix,b)

        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5]
            result += matrix[r2][(c2 - 1) % 5]

        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1]
            result += matrix[(r2 - 1) % 5][c2]

        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


key = input("Enter the keyword: ")
matrix = gen_key_matrix(key)
print_matrix(matrix)

msg = input("Enter the message to encrypt: ")
enc = playfair_encrypt(msg,matrix)
dec = playfair_decrypt(enc,matrix)

print("Original message: ",msg.upper())
print("Encrypted message: ",enc)
print("Decrypted message: ",dec)

            
