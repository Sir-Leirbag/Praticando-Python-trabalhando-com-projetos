def calcula_digito(cpf, fatores):
    cpf_convertido = [int(digito) * fator for digito, fator in zip(cpf, fatores)]
    soma = sum(cpf_convertido)
    resto = soma % 11
    if resto < 2:
        return 0
    return 11 - resto

def valida_cpf(cpf):
    if not cpf.isdigit():
        return 'Erro: O CPF deve conter apenas números.'
    if len(cpf) != 11:
        return 'Erro: O CPF deve ter exatamente 11 dígitos.'
    if cpf == cpf[0] * 11:
        return 'Erro: CPF inválido.'
    if (
        int(cpf[9]) != calcula_digito(cpf, range(10, 1, -1)) 
        or int(cpf[10]) != calcula_digito(cpf, range(11, 1, -1))
    ):
        return 'Erro: CPF inválido.'
    return 'CPF válido.'

cpf = input('Digite seu CPF: ')

print(valida_cpf(cpf))
