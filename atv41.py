def contar_caracteres(texto):
    contagem = {}

    for caractere in texto:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1

    return contagem

print(contar_caracteres("abacaxi"))