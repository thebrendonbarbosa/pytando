"""
 Listas e Tuplas
 """



#

lista_A = ['Arroz','Carne','Sal']



"""
Tuplas são imutáveis
Usando quando nao preciso editar oos itens 
"""
tupla = 'Abóbora' , 'Carangueijo', 'Salada'
tupla_2 = ('Arroz' , 'Carne', 'Sal')

print(tupla[-1])



# Converter lista em tupla

tupla_3 = tuple(lista_A)
print(tupla_3)


# Converter tupla em lista

lista_B = list(tupla)
print(lista_B)