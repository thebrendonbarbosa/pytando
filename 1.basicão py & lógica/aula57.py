"""
enumerate - enumera iteráveis (indices)
Cria um tupla com o indice e o valor
"""


lista = ["abacate", "bola", "cachorro"]
lista.append("dinheiro")

print(lista)

#Enumerando a lista
lista_enumerada = enumerate(lista)
print(list(lista_enumerada))

lista_enumerada2 = list(enumerate(lista,start=5)) # Começa a enumerar a partir do 5
print(lista_enumerada2)

for indice, valor in lista_enumerada:
    print(indice, valor)


for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])