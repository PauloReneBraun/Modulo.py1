# Declaracao 

minha_lista = [1, 2, 3, 4, 5, "OW", True, False]

print("Minha lista de exemplo", minha_lista)

# Exibindo a lista 
minha_lista[0] = "Python"
print("minha lista[0]:",minha_lista)

print("minha lista[0]:",minha_lista[0])
print("minha lista[5]:",minha_lista[5])
print("minha lista[1:7]:",minha_lista[1:7])
print("minha lista[:]:",minha_lista[:5])
print("minha lista[2:]:",minha_lista[2:])

#Método de lista 

#Método append(): Adiciona um elemento no final da lista 
minha_lista.append(6)
print("Após append(6):", minha_lista)

#Método index 
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

#Método insert: Insere um elelmento ao final da lista
minha_lista.insert(2, 10)
print("Após insert(2, 10):", minha_lista)

#Método pop
elemento_removido = minha_lista.pop(3)
print("Elelmento removido:", elemento_removido)
print("Após pop(3)")