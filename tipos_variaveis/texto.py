# Declarar 
nome_completo = "Paulo Braun"

nome_completo_aspas = """Paulo 
Braun"""

nome_completo_quebra = "Paulo \
Braun"

nome = "Paulo"
sobrenome = "Braun"

# Formatação
print("nome_completo(1° forma):", nome_completo)
print("nome_completo(2° forma):" + nome_completo)
print("nome_completo(3° forma):" + "Paulo" + "Braun")
print("nome_completo(4° forma):" + "Paulo" , "Braun")
print("nome_completo(5° forma):", nome_completo_aspas)
print("nome_completo(6° forma):", nome_completo_quebra)
print("nome_completo(7° forma): %s" %nome_completo)
print("nome_completo(8° forma): %s %s" %(nome, sobrenome))
print(f"nome_completo(9° forma): {nome} {sobrenome}")
print("nome_completo(10° forma): {} {}".format(nome,sobrenome))