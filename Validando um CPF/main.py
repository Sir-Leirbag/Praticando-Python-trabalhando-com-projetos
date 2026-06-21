# 1. Funções
def converte_cpf(cpf):
    return [int(d) for d in list(cpf)]

# 2. Entrada de dados
cpf = list(input('Digite seu CPF: '))

# 3. Processamento
try:
    digitos = converte_cpf(cpf)
except ValueError:
    print('O CPF deve conter apenas números.')
    quit()

if len(digitos) != 11:
    print('O CPF deve ter exatamente 11 dígitos.')
else:
    print('CPF válido.')
