import random

def gerar_elemento():
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    return random.choice(opcoes)

#def limpar_entrada(elemento):
#    elemento = elemento.islower()

elemento = input('Escolha: Pedra, Papel ou Tesoura? ')
jogada_computador = gerar_elemento()

if elemento == jogada_computador:
    print(f'O computador escolheu: {jogada_computador}')
    print('Empate!')
elif elemento == 'Pedra' and jogada_computador == 'Tesoura':
    print(f'O computador escolheu: {jogada_computador}')
    print('Você venceu!')
elif elemento == 'Pedra' and jogada_computador == 'Papel':
    print(f'O computador escolheu: {jogada_computador}')
    print('O computador venceu!')
elif elemento == 'Papel' and jogada_computador == 'Pedra':
    print(f'O computador escolheu: {jogada_computador}')
    print('Você venceu!')
elif elemento == 'Papel' and jogada_computador == 'Tesoura':
    print(f'O computador escolheu: {jogada_computador}')
    print('O computador venceu!')
elif elemento == 'Tesoura' and jogada_computador == 'Papel':
    print(f'O computador escolheu: {jogada_computador}')
    print('Você venceu!')
elif elemento == 'Tesoura' and jogada_computador == 'Pedra':
    print(f'O computador escolheu: {jogada_computador}')
    print('O computador venceu!')
else:
    print('Jogada inválida')
