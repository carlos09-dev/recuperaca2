def eh_palindromo(texto):
    texto_limpo = ""

    for letra in texto.lower():
        if letra != " ":
            texto_limpo += letra

    return texto_limpo == texto_limpo[::-1]

print(eh_palindromo("A base do teto desaba"))