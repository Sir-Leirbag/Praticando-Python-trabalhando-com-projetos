# 1. Funções e classes
def calcular_gorjeta(conta, porcentagem):
    return conta * (porcentagem / 100)

def calcular_total(conta, gorjeta):
    return conta + gorjeta

class ValorNegativo(Exception):
    pass

# 2. Entrada de dados e tratamento de erros
try:
    conta = float(input('Digite o valor total da conta: R$ '))
    porcentagem = float(input('Digite a porcentagem de gorjeta: '))
    if conta < 0 or porcentagem < 0:
        raise ValorNegativo('Digite valores maiores ou iguais a zero.')
except ValueError:
    print('Digite apenas números.')
    exit()
except ValorNegativo as erro:
    print(erro)
    exit()

# 3. Processamento
valor_da_gorjeta = calcular_gorjeta(conta, porcentagem)
total = calcular_total(conta, valor_da_gorjeta)

# 4. Saída
print(f'Valor da gorjeta: R$ {valor_da_gorjeta:.2f}')
print(f'Total a pagar: R$ {total:.2f}')
