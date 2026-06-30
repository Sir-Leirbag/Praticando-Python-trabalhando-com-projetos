def adicionar_tarefa(tarefa_adicionada):
    tarefa_adicionada = input('\nDigite a tarefa que deseja adicionar: ')
    lista_de_tarefas.append(tarefa_adicionada)
    print(f'Tarefa {tarefa_adicionada} adicionada!')

def visualizar_tarefas(lista_de_tarefas):
    print('\nTarefas:')
    for i, tarefa in enumerate(lista_de_tarefas, start=1):
        print(f'{i}. {tarefa}')

def remover_tarefa(tarefa_removida):
    tarefa_removida = int(input('\nDigite o número da tarefa a ser removida: '))
    indice = tarefa_removida - 1
    tarefa_removida = lista_de_tarefas.pop(indice)    
    print(f'Tarefa {tarefa_removida} removida.')

lista_de_tarefas = []

def main():
    while True:
        tarefa = ''
        opcoes = (1, 2, 3, 4)
        try:
            opcao = int(input(                         
'''\n1. Adcionar tarefa
2. Visualizar tarefas
3. Remover tarefa
4. Sair
Escolha uma opcão: '''))
        except ValueError:
            print('\nOpção inválida.')
            continue
        if opcao not in opcoes:
            print('Opcão inválida.')
            continue
        elif opcao == 1:
            adicionar_tarefa(tarefa)
            continue
        elif opcao == 2:
            visualizar_tarefas(lista_de_tarefas)
            continue
        elif opcao == 3:
            remover_tarefa(tarefa)
        elif opcao == 4:
            print('\nSaindo do gerenciador de tarefas. Até mais!')
            break

main()
