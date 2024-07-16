import numpy as np


def gauss_jordan_mod2(A, b):
    n = len(A)
    A = np.array(A, dtype=int)
    b = np.array(b, dtype=int)

    # Eliminação gaussiana
    for j in range(n):
        if A[j, j] == 0:  # Se o pivot é 0, troca de linha
            for i in range(j + 1, n):
                if A[i, j] == 1:
                    A[[j, i]] = A[[i, j]]
                    b[j], b[i] = b[i], b[j]
                    break

        if A[j, j] == 0:  # Se não encontrar linha para trocar, pula para a próxima coluna
            continue

        # Achou o pivot, começamos zerando as linhas com mod 2
        for i in range(n):
            if i != j and A[i, j] == 1:
                # Podemos somar já que é mod 2
                A[i] = (A[i] + A[j]) % 2
                b[i] = (b[i] + b[j]) % 2

    # Verificando se tem solução
    for i in range(n):
        if A[i, i] == 0 and b[i] == 1:
            print("[Erro] Sem solução")
            return
    return A, b
