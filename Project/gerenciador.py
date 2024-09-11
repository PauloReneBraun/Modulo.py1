def adicionar_tarefa(tarefas, nome_tarefa="tarefa padrão"):

  # TAREFA: NOME DA TAREFA
  # COMPLETADA: indica se a tarefa foi completada ou não

  tarefa = { "tarefa": nome_tarefa, "completada": False }

  tarefas.append(nome_tarefa)
  print(f"Tarefa {nome_tarefa} foi Adicionando ")
  return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
  tarefas[indice_tarefa]["tarefa"] = novo_nome_tarefa
  print(f"Tarefa {indice_tarefa} foi atualizada para {novo_nome_tarefa}")
  return


tarefas = []

while True:
  print("\nMenu do Gerenciador de tarefas:")
  print("1. Adicionar tarefa")
  print("2. Ver tarefas")
  print("3. Atualizar tarefa")
  print("4 Completar tarefa")
  print("5. Deletar tarefa completas")
  print("6. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa: ")
    adicionar_tarefa(tarefas, nome_tarefa =nome_tarefa)
  elif escolha == "2":
    ver_tarefas(tarefas)
  elif escolha == "3":
    ver_tarefas(tarefas)
    indice_tarefa = int(input("Digite o índice da tarefa que deseja atualizar: "))
    novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
  if escolha == "6":
    break

print("Programa Finalizado")