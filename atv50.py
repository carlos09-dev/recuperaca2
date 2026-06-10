def multiplicacao(a, b):
    resultado = 0
    negativo = False

    if a < 0:
        a = -a
        negativo = not negativo

    if b < 0:
        b = -b
        negativo = not negativo

    for _ in range(b):
        resultado += a

    if negativo:
        resultado = -resultado

    return resultado

print(multiplicacao(6, 7))    
print(multiplicacao(-6, 7))   
print(multiplicacao(6, -7))   
print(multiplicacao(-6, -7))  
print(multiplicacao(0, 5))