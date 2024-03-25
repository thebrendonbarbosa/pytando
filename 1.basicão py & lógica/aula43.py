
"""
Laço de repetição for
è uma estrutura de repetição que percorre uma sequência de elementos
"""

texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra} '
    print(letra)

print(novo_texto +'*')