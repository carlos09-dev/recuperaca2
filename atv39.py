def soma_digitos(numero):
    soma = 0

    for digito in str(numero):
        soma += int(digito)

    return soma

print(soma_digitos(12345))