def poly_mul_list(a, b):
    # Multiply two polynomials a(x), b(x) over GF(2), LSB-first
    res = [0] * (len(a) + len(b) - 1)  # maximum degree = deg(a)+deg(b)

    for i in range(len(a)):
        for j in range(len(b)):
            res[i + j] ^= a[i] * b[j]  # XOR = addition mod 2

    # trim trailing zeros (remove high-degree 0's)
    while len(res) > 1 and res[-1] == 0:
        res.pop()

    return res

A = list(map(int, input("Enter polynomial A as bits (LSB first): ")))
B = list(map(int, input("Enter polynomial B as bits (LSB first): ")))

result = poly_mul_list(A, B)

print("\nPolynomial A:", A)
print("Polynomial B:", B)
print("A(x) * B(x) =", result)
