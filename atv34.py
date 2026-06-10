def intersecao_listas(lista1, lista2):
    resultado = []

    for elemento in lista1:
        if elemento in lista2 and elemento not in resultado:
            resultado.append(elemento)

    return resultado

print(intersecao_listas([1, 2, 3, 4], [3, 4, 5, 6]))