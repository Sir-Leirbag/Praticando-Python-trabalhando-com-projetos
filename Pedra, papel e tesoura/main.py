import random

opcoes = ['pedra', 'papel', 'tesoura']

def gerar_elemento():
    return random.choice(opcoes)

elemento = input('Escolha: pedra, papel ou tesoura? ')
jogada_usuario = elemento.strip().lower()

if jogada_usuario not in opcoes:
    print('Jogada inválida')
else:
    jogada_computador = gerar_elemento()
    print(f'O computador escolheu: {jogada_computador}')

    if jogada_usuario == jogada_computador:
        print('Empate!')
    elif (
        jogada_usuario == 'pedra' and jogada_computador == 'tesoura'
        or jogada_usuario == 'papel' and jogada_computador == 'pedra'
        or jogada_usuario == 'tesoura' and jogada_computador == 'papel'
    ):
        print('Você venceu!')
    else:
        print('O computador venceu!')
