"""
Ask the user to enter an integer that is over 500. Work
out the square root of that number and display it to two
decimal places."""

import math

num = input('Digite um número maior que 500: ')
num_float = float(num)

if num_float > 500:
    raiz = math.sqrt(num_float)
    print(f'A raiz de {num_float} é {raiz:.2f}!')
else: 
    print('Erro! Informe um número maior que 500.')
