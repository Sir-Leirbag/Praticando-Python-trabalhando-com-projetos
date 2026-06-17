# 1. Funções
def calcular_gorjeta(conta, porcentagem):
    return conta * (porcentagem / 100)

def calcular_total(conta, gorjeta):
    return conta + gorjeta

# 2. Entrada de dados
conta = float(input('Digite o valor total da conta: R$ '))
porcentagem = float(input('Digite a porcentagem de gorjeta: % '))

# 3. Processamento
valor_da_gorjeta = calcular_gorjeta(conta, porcentagem)
total = calcular_total(conta, porcentagem)

#4. Saída
print(f'\nValor da gorjeta: R$ {valor_da_gorjeta:.2f}')
print(f'Total a pagar: R$ {total:.2f}')
