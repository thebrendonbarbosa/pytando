"""

Interando strings com while
"""


nome = 'Brendon Barbosa'

tamanho_nome = len(nome)

# print(nome[0],tamanho_nome, nome)

indice = 0
novo_nome = ''

while indice < tamanho_nome:
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice +=1
novo_nome += '*'

print(novo_nome)