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