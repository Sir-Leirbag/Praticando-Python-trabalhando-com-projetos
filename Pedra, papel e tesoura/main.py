import random

def gerar_elemento():
    return random.choice(opcoes)

def usuario_venceu(usuario, computador):
    return (
        usuario == 'pedra' and computador == 'tesoura'
        or usuario == 'papel' and computador == 'pedra'
        or usuario == 'tesoura' and computador == 'papel'
    )

opcoes = ('pedra', 'papel', 'tesoura')
elemento = input('Escolha: pedra, papel ou tesoura? ')
jogada_usuario = elemento.strip().lower()

if jogada_usuario not in opcoes:
    print('Jogada inválida')
else:
    jogada_computador = gerar_elemento()
    print(f'O computador escolheu: {jogada_computador}')

    if jogada_usuario == jogada_computador:
        print('Empate!')
    elif usuario_venceu(jogada_usuario, jogada_computador):
        print('Você venceu!')
    else:
        print('O computador venceu!')
