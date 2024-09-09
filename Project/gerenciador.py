def adicionar_tarefa(nome_tarefa, tarefas):

  # TAREFA: NOME DA TAREFA
  # COMPLETADA: indica se a tarefa foi completada ou não

  tarefa = { "tarefa": nome_tarefa, "completada": False }

  tarefas.append(nome_tarefa)
  print(f"Tarefa {nome_tarefa} foi Adicionando ")
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
    adicionar_tarefa(nome_tarefa, tarefas)

  if escolha == "6":
    break

print("Programa Finalizado")