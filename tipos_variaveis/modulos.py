print("Exemplo de importação de um módulo padrão:")
from math import sqrt

raiz_quadrada = sqrt(16)
print(raiz_quadrada)

print("\nExemplo de importação de um módulo personalizado:")
from meu_modulo import saudacao, dobro

mensagem = meu_modulo.saudacao("Mundo")
resultado_dobro = meu_modulo.dobro(5)
print(mensagem)
print(f"O dobro de 5 é {resultado_dobro}")