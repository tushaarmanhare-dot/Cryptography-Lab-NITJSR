def poly_str_to_int(s):
    """Convert string like '1101' (LSB first) into integer."""
    return int(s[::-1], 2)   #reverse because input is LSB-first

def poly_mul_mod(a, b, mod_poly):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
    #Final reduction step
    while result.bit_length() >= mod_poly.bit_length():
        shift = result.bit_length() - mod_poly.bit_length()
        result ^= (mod_poly << shift)
    return result

#User Input
A_str = input("Enter polynomial A as bits (LSB first): ")
B_str = input("Enter polynomial B as bits (LSB first): ")
M_str = input("Enter modulus polynomial as bits (LSB first): ")

#Convert to integers
A = poly_str_to_int(A_str)
B = poly_str_to_int(B_str)
M = poly_str_to_int(M_str)

#Multiply modulo
res = poly_mul_mod(A, B, M)

#Print results
print("\nPolynomial A:", A_str)
print("Polynomial B:", B_str)
print("Modulus Poly:", M_str)
print("Result (binary, LSB first):", bin(res)[2:][::-1])

