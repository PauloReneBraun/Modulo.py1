#Criando um dicionário de exemplo 
pessoa = {"nome": "Mateus", "idade": 20, "cidade": "Curitiba"}

#exibindo o dicionario 
print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chave 
print("Nome :" , pessoa["nome"])
print("Idade :" , pessoa["idade"])
print("Cidade :" , pessoa["cidade"])

pessoa["sobrenome"] = "Correia"
print("Sobrenome :" , pessoa["sobrenome"])