print("As capturas de execessões")
try:
  numero = input(input("Digite um número: ") )
  resultado = 10 / int(numero)
  print(f"resultado: {resultado}")
except ValueError as e:
    print(f"Erro: {e}")
    raise ValueError("Erro: {e}")
except ZeroDivisionError as e:
    print(f"Erro: {e}")
except Exception as e:
  print("Erro: {e}")
else:
  print("Tudo ocorreu bem")
finally:
  print("Finalizando o programa")