"""Create a list of two sports. Ask the
user what their favourite sport is and
add this to the end of the list. Sort the
list and display it. """

lista_de_esportes = ['Vôlei', 'Natação']

esporte_favorito_user = input('Informe seu esporte favorito: ')

lista_de_esportes.append(esporte_favorito_user)
lista_de_esportes.sort()

print(lista_de_esportes)
