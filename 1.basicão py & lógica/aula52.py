
"""
Cuidados com dados mutaveis
  = - copiado o valor (imutáveis)
  = - aponta para o mesmo valor da memorória (mutável)
"""

lista_a = ['Luiz', 'Maria', 1, True, 1.2]

# Lista b aponta para o mesmo endereço
lista_b = lista_a
"""
Nesse caso, o que for alterado na lista a será também
na lista b
"""
lista_a[0] = 'Novo mundo'
print(lista_b)


# Copiando listas sem afetar outra

lista_c = lista_a.copy()
print(lista_c)