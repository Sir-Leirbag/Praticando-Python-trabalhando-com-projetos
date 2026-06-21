def primeiro_digito(cpf):
    fatores = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    # Separa os dígitos e multiplica cada um pelo seu fator correspondente
    cpf_convertido = [int(digito) * fator for digito, fator in zip(cpf, fatores)]
    soma = sum(cpf_convertido)
    resto = soma % 11
    if resto < 2:
        return 0
    else:
        return 11 - resto
        

def valida_cpf(cpf):
    if not cpf.isdigit():
        return('Erro: O CPF deve conter apenas números.')
    if len(cpf) != 11:
        return 'Erro: O CPF deve ter exatamente 11 dígitos.'
    if cpf == cpf[0] * 11:
        return 'Erro: CPF inválido.'
    return 'CPF válido.'

cpf = input('Digite seu CPF: ')

print(valida_cpf(cpf))
print(primeiro_digito(cpf))