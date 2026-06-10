def soma_indices_pares(lista):
    soma = 0

    for i in range(0, len(lista), 2):
        soma += lista[i]

    return soma

print(soma_indices_pares([1, 2, 3, 4, 5, 6]))