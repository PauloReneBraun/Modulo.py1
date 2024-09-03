print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
for elementor in lista:
  print(elementor)

print("For utilizando tupla")
tupla = (2, 3, 4, 5, 6)
for elemento in tupla:
    print(elemento)

pessoa = {"nome": "Juca", "idade": 70, "cidade": "Curitiba"}
print("For utilizando dicionario - chaves")
for chave in pessoa.keys():
   print(chave)

print("For utilizando dicionario - valores")
for valor in pessoa.values():
   print(valor)

print("For utilizando dicionario - items")
for chave, valor in pessoa.items():
   print(f"{chave}: {valor}")

# range(): Intervalo numérico
# [0, 1,2,3,4,5,6,7,8,9]

print("\n Utilizando a função range()")
for numero in range(5):
   print("Numero:", numero)

print("\n Utilizando a função range() com len()")
lista = [1, 3, 4, 5, 6]
for indice in range(0, len(lista)):
   print("Indice:", indice)
   print("Elemento:", lista[indice])
   if indice == 3:
      lista[indice] = 5
   else:
      lista[indice] = 0 
print(lista)

# enumerate()
lista_enumarate = ["D", "E", "F"]
for indice, valor in enumerate(lista_enumarate):
   print(f"{indice}: {valor}")