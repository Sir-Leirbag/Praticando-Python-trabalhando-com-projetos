conta = float(input('Digite o valor total da conta: R$ '))
porcentagem = float(input('Digite a porcentagem de gorjeta: % '))

def calcular_gorjeta (porcentagem, conta):
    valor_da_gorjeta = conta * (porcentagem / 100)
    return valor_da_gorjeta

def calcular_total (conta, porcentagem):
    total = conta + calcular_gorjeta(porcentagem, conta)
    return total

valor_da_gorjeta = calcular_gorjeta(porcentagem, conta)
total = calcular_total(conta, porcentagem)

print(f'\nValor da gorjeta: R$ {valor_da_gorjeta:.2f}')
print(f'Total a pagar: R$ {total:.2f}')
