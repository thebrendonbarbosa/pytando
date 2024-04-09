"""Display a 
random 
fruit from 
a list of 
five fruits. """

import random as rd

lista_frutas = ['Banana', 'Laranja', 'Uva', 'Maçã', 'Pera']

fruta_sorteada = rd.choice(lista_frutas)

print(f'A fruta sorteado foi {fruta_sorteada}!')
