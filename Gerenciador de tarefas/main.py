def adicionar_tarefa(tarefa_adicionada):
    tarefa_adicionada = input('\nDigite a tarefa que deseja adicionar: ')
    lista_de_tarefas.append(tarefa_adicionada)
    print(f'Tarefa {tarefa_adicionada} adicionada!')

def visualizar_tarefas(lista_de_tarefas):
    print('\nTarefas:')
    for i, tarefa in enumerate(lista_de_tarefas, start=1):
        print(f'{i}. {tarefa}')

def remover_tarefa(tarefa_removida):
    while True:
        try:
            tarefa_removida = int(input('\nDigite o número da tarefa a ser removida:'))
            if not lista_de_tarefas:
                print('Erro: Nenhuma tarefa para remover.')
                break
            else:
                indice = tarefa_removida - 1
                tarefa_removida = lista_de_tarefas.pop(indice)    
                print(f'Tarefa {tarefa_removida} removida.')
        except ValueError:
            print('Erro: Entrada inválida! Digite um número.')
            continue
        except IndexError:
            if len(lista_de_tarefas) == 1:
                print(f'Erro: Opção inválida! Há apenas 1 opção.')
            if len(lista_de_tarefas) > 1:
                print(f'Erro: Opção inválida! Escolha uma opcão entre 1 e {len(lista_de_tarefas)}.')
            continue            
        break

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
