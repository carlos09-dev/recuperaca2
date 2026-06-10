def inverter_palavras(frase):
    palavra_atual = ""
    resultado = ""

    for caractere in frase:
        if caractere != " ":
            palavra_atual = caractere + palavra_atual
        else:
            resultado += palavra_atual + " "
            palavra_atual = ""

    resultado += palavra_atual  # última palavra

    return resultado

print(inverter_palavras("Olá mundo"))