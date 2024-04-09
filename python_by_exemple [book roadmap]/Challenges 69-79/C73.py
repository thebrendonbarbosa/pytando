"""Ask the user to enter four of their
favourite foods and store them in
a dictionary so that they are
indexed with numbers starting
from 1. Display the dictionary in
full, showing the index number
and the item. Ask them which they
want to get rid of and remove it
from the list. Sort the remaining
data and display the dictionary. """

lista_comidas_entrada = []

for i in range(4):
    comidas_entrada = input('Informe uma comida favorita sua: ')
    lista_comidas_entrada.append(comidas_entrada)
dic_comidas = {
    '1': lista_comidas_entrada[0],
    '2': lista_comidas_entrada[1],
    '3': lista_comidas_entrada[2],
    '4': lista_comidas_entrada[3],
}
print(dic_comidas)

comida_remover = input('informe o número da comida a ser removida: ')

del dic_comidas[comida_remover]

print(f'Certo, a comida removida com sucesso!')
print(dic_comidas)