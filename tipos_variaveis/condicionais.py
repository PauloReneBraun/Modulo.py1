# if, elif e else

# exemplo if
idade = input("Quantos anos você tem? ")
print("Exemplo de comando if")
if idade >= 18:
  print("Você é maior de idade.")
elif idade >= 12:
  print("Você é um adolecente")
else:
  print("Você é menor de idade")

if idade == 20:
  print("Você tem 20 anos")

if idade <= 18: 
  print("Você é menor d idade")

if idade != 10:
  print("Você não tem 10 anos")

  mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Você não pode dirigir"

  print(mensagem)