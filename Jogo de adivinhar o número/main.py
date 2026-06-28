import random

def gerar_numero_aleatorio():
    lista = tuple(range(1,101))
    numero_aleatorio = random.choice(lista)
    return numero_aleatorio

def comparar_numero(numero):
    if numero < 0 or numero > 100:
        print('Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.')
        main()
    elif numero > numero_aleatorio:
        print(f'Muito alto! Tente novamente: {numero}')
        main()
    elif numero < numero_aleatorio:
        print(f'Muito baixo! Tente novamente: {numero}')
        main()
    else:
        print(f'Parabéns! Você acertou o número: {numero}')

def main():
    try:
        numero = int(input('Tente adivinhar o número (1-100): '))
    except ValueError:
        print('Entrada inválida: Digite apenas números.')
        main()
    comparar_numero(numero)

numero_aleatorio = gerar_numero_aleatorio()
main()