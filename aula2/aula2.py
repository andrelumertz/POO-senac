"""
Crie uma função que retorne quantos caracteres há em uma string
"""

def conta_caracteres(string):
    return len(string)
print(conta_caracteres("olá"))  


"""
Crie uma função que receba um número inteiro como parâmentro e
retorne quantos dígitos há neste número
"""

def numero_de_digitos(numero):
    return len(str(numero))

print(numero_de_digitos(30))

"""
Crie uma função que receba um número inteiro como parâmetro e
retorne esse número invertido
"""

def inverte_num(numero):
    return int(str(numero)[::-1])



"""
Crie uma função que retorne uma lista com 10 números inteiros entre
10 e 1000
"""

def lista_de_numeros():
    import random
    lista = []
    for i in range(10):
        numero = random.randint(10, 1000)
        lista.append(numero)
    return lista