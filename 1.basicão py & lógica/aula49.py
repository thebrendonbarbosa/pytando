"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300 # Muda o valor de um item da list

# del lista[2] # deleta um item da lista e a lista dimuniu movento os item

# print(lista)
# print(lista[2])
lista.append(50) # Adiciona  o argumento na lista

lista.pop()  # Remove o ultimo elemento da lista

lista.append(60)
lista.append(70)

ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)