import random

def gerar_numero_aleatorio():
    return random.randint(1,100)

numero_aleatorio = gerar_numero_aleatorio()
tentativas = 0

while True:
    try:
        numero = int(input('Tente adivinhar o número (1-100): '))
    except ValueError:
        print('Entrada inválida: Digite apenas números.')
        continue
    tentativas += 1
    if 1 > numero > 100:
        print('Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.')
    elif numero > numero_aleatorio:
        print(f'Muito alto! Tente novamente: {numero}')
    elif numero < numero_aleatorio:
        print(f'Muito baixo! Tente novamente: {numero}')
    else:
        print(f'Parabéns! Você acertou o número: {numero} com {tentativas} tentativas.')
        break
