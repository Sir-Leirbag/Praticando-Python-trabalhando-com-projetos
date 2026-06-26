import random

def gerar_senha(senha):
    for i in range(12):
        senha.append((random.choice(elementos)))

def validar_senha(senha):
    if (any(elemento.islower() for elemento in senha)
        and any(elemento.isupper() for elemento in senha)
        and any(elemento.isdigit() for elemento in senha)
        and any(not elemento.isalnum() for elemento in senha)
        ):
        return True
    else:
        return False

def main():
    senha = []
    gerar_senha(senha)
    if validar_senha(senha) == False:
        senha = []
        main()
    else:
        print(f"Senha gerada: {''.join(senha)}")


elementos = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*?,.')

main()
