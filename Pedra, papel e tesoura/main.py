import random

def gerar_elemento():
    opcoes = ['pedra', 'papel', 'tesoura']
    return random.choice(opcoes)

def limpar_entrada(elemento):
    return elemento.strip().lower()

elemento = input('Escolha: pedra, papel ou tesoura? ')
jogada_computador = gerar_elemento()
jogada_usuario = limpar_entrada(elemento)

if jogada_usuario == jogada_computador:
    print(f'O computador escolheu: {jogada_computador}')
    print('Empate!')
elif jogada_usuario == 'pedra' and jogada_computador == 'tesoura':
    print(f'O computador escolheu: {jogada_computador}')
    print('Você venceu!')
elif jogada_usuario == 'pedra' and jogada_computador == 'papel':
    print(f'O computador escolheu: {jogada_computador}')
    print('O computador venceu!')
elif jogada_usuario == 'papel' and jogada_computador == 'pedra':
    print(f'O computador escolheu: {jogada_computador}')
    print('Você venceu!')
elif jogada_usuario == 'papel' and jogada_computador == 'tesoura':
    print(f'O computador escolheu: {jogada_computador}')
    print('O computador venceu!')
elif jogada_usuario == 'tesoura' and jogada_computador == 'papel':
    print(f'O computador escolheu: {jogada_computador}')
    print('Você venceu!')
elif jogada_usuario == 'tesoura' and jogada_computador == 'pedra':
    print(f'O computador escolheu: {jogada_computador}')
    print('O computador venceu!')
else:
    print('Jogada inválida')
