#Exemplo 
def saudacao(nome):
  print(f"Olá, {nome}!")

print("\n Chamando a função saudacao:")

# Funcao com retorno
def quadrado(numero):
  resultado = numero ** 2
  return resultado

print("\n Chamando função quadrado:")
resultado_quadrado = quadrado(5)
print("Resultado da funcao quadrado:", resultado_quadrado)

# Funcao com multiplos parametos 
def soma(numero1, numero2):
  resultado = numero1 + numero2
  return resultado