# 1. Funções
def separa_digitos(cpf):
    return [int(d) for d in str(cpf)]

# 2. Entrada de dados
try:
    cpf = int(input('Digite seu CPF: '))
except ValueError:
    print('Digite apenas números')
    quit()

# 3. Processamento
digitos = separa_digitos(cpf)

if len(digitos) != 11:
    print('O CPF deve ter exatamente 11 dígitos.')
else:
    print('CPF válido.')
