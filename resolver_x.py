import numpy as np

from criar_A import criar_A
from gauss_jordan_mod2 import gauss_jordan_mod2

n = 5
b = np.array([
    1, 0, 1, 0, 1,
    1, 0, 1, 0, 1,
    1, 1, 0, 0, 0,
    0, 0, 0, 1, 1,
    1, 0, 1, 0, 1], dtype=int)

b = np.array(b)

A = criar_A(n)

A, b = gauss_jordan_mod2(A, b)

# Como linalg.solve não funciona para mod 2, vamos resolver manualmente
x = np.zeros(n*n, dtype=int)
for i in range(n*n - 1, -1, -1):
    x[i] = b[i]
    for j in range(i + 1, n*n):
        x[i] = (A[i, j]*x[j] - x[i]) % 2

print(x.reshape(n, n))
