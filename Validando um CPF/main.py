def valida_cpf(cpf):
    if not cpf.isdigit():
        return('Erro: O CPF deve conter apenas números.')
    if len(cpf) != 11:
        return 'Erro: O CPF deve ter exatamente 11 dígitos.'
    if cpf == 00000000000 or 12345678901 or 11111111111:
        return('Erro: CPF inválido.')
    return 'CPF válido.'

cpf = input('Digite seu CPF: ')

print(valida_cpf(cpf))
