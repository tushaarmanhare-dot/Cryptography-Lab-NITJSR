def poly_add_list(a, b):
    # a, b are lists of bits LSB-first, e.g. x^3+x+1 -> [1,1,0,1]
    n = max(len(a), len(b))
    res = []
    for i in range(n):
        if i < len(a):
            ai = a[i]
        else:
            ai = 0
        if i < len(b):
            bi = b[i]
        else:
            bi = 0

        res.append(ai ^ bi)   # XOR = addition mod 2

    # trim trailing zeros (remove high-degree 0's)
    while len(res) > 1 and res[-1] == 0:
        res.pop()

    return res

A = list(map(int, input("Enter polynomial A as bits (LSB first): ")))
B = list(map(int, input("Enter polynomial B as bits (LSB first): ")))

result = poly_add_list(A, B)

print("\nPolynomial A:", A)
print("Polynomial B:", B)

print("A(x) + B(x) =", result)
