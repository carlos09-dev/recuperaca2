def contar_vogais(texto):
    vogais = "aeiou"
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1

    return contador

print(contar_vogais("Programação"))