#PROBLEMA: Faça a soma de dois números digitados pelo usuário

def somar (a, b):
    return a + b

def main ():
    try:
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))

        resultado = somar(numero1, numero2)

        print(f'A soma é: {resultado}')
    except ValueError:
        print('Erro: Digite apenas números válidos!')
        main()

main()