def segundo_maior(lista):
    maior = lista[0]
    segundo = lista[0]

    for numero in lista:
        if numero > maior:
            segundo = maior
            maior = numero
        elif numero > segundo and numero != maior:
            segundo = numero

    return segundo

print(segundo_maior([10, 20, 4, 45, 99, 99]))