#Criando um dicionário de exemplo 
pessoa = {"nome": "Mateus", "idade": 19, "cidade": "Curitiba"}

#exibindo o dicionario 
print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chave 
print("Nome :" , pessoa["nome"])
print("Idade :" , pessoa["idade"])
print("Cidade :" , pessoa["cidade"])

pessoa["sobrenome"] = "Correia"
print("Sobrenome :" , pessoa["sobrenome"])

pessoa["idade"] = 20
print("Idade atualizada:", pessoa["idade"])

# Removendo um par
del pessoa["sobrenome"]
print("Meu dicionário de exemplo:", pessoa)

#Método: keys(), values(), items()
chaves = pessoa.keys()
print("Chaves do dicionário:", chaves)
print("Pirmeira chave:", chaves[0])