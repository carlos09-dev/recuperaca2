def remover_duplicados(s):
    resultado = ""
    for c in s:
        if c not in resultado:
            resultado += c
    return resultado

print(remover_duplicados("banana"))  