# Set - Conjunto de dados em Python
# Conjunto são ensinados na matematica
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Vein
# Sets são mutáveis, porem aceitam apenas tipos imutaveis como valor interno

# Criando um set
# set(iteravel) ou {1,2,3}

set1 = set() # Vazio
set2 = set('Barsi')
set3 ={'Brendon',12,1,1110} # com dados
#print(set2,set3)

# São eficientes para remover valores duplicados de iteráveis
# Seus valores serão sempre unicos
# Nao aceitam valores mutaveis
# Nao tem indexes
# Nao garantem ordem
# sao iteraveis (for, in, not in)

set4 = {1,2,3,3,3,3,3,4}
# SEts eliminam valores duplicados



# remover item duplicado de listas

#metodo 1
lista1 = [1, 2,4,1,2,4]
set_lista1 = set(lista1)
lista_1_by_set = list(set_lista1) #Pode nao garantir a ordem
print(set_lista1)#,lista_1_by_set)
print(2 in set_lista1)

