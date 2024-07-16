import numpy as np


def criar_A(n):
    A = np.zeros((n*n, n*n), dtype=int)

    for linha in range(n):
        for col in range(n):
            i = linha*n + col

            # própria célula
            A[i, i] = 1

            # célula de cima
            if linha > 0:
                A[i, i - n] = 1

            # célula de baixo
            if linha < n - 1:
                A[i, i + n] = 1

            # célula da esquerda
            if col > 0:
                A[i, i - 1] = 1

            # célula da direita
            if col < n - 1:
                A[i, i + 1] = 1

    return A
