import random

def gerar_numero_aleatorio():
    lista = tuple(range(1,101))
    numero_aleatorio = random.choice(lista)
    return numero_aleatorio

#numero = int(input('Tente adivinhar o número (1-100): '))

print(gerar_numero_aleatorio())