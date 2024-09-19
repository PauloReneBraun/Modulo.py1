print("As capturas de execessões")
try:
  numero = input(input("Digite um número: ") )
  resultado = 10 / int(numero)
  print(f"resultado: {resultado}")
except Exception as e:
  print("Erro: {e}")
