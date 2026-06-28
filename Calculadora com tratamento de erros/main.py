def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

def formatar_resultado(resultado):
    if resultado.is_integer():
        return int(resultado)
    return round(resultado, 2)

def main():
    while True:
        try:
            primeiro_numero = float(input('Digite o primeiro número: '))
            operacao = input('Escolha a operação (+, -, *, /): ')
            if operacao not in ('+', '-', '*', '/'):
                print('Operação inválida.')
                continue
            segundo_numero = float(input('Digite o segundo número: '))
        except ValueError:
            print('Erro: Entrada inválida. Digite apenas números.')
            continue
        if operacao == '+':
            resultado = soma(primeiro_numero, segundo_numero)
            print(f'Resultado: {formatar_resultado(resultado)}')
        elif operacao == '-':
            resultado = subtracao(primeiro_numero, segundo_numero)
            print(f'Resultado: {formatar_resultado(resultado)}')
        elif operacao == '*':
            resultado = multiplicacao(primeiro_numero, segundo_numero)
            print(f'Resultado: {formatar_resultado(resultado)}')
        elif operacao == '/':
            if segundo_numero != 0:
                resultado = divisao(primeiro_numero, segundo_numero)
                print(f'Resultado: {formatar_resultado(resultado)}')
            else:
                print('Erro: Divisão por zero não é permitida.')
                continue
        break

main()
