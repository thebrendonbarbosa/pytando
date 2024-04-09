"""
Ask the user to enter two numbers.
Use whole number division to divide
the first number by the second and
also work out the remainder and
display the answer in a user-friendly
way (e.g. if they enter 7 and 2 display
“7 divided by 2 is 3 with 1
remaining”).
"""

import math

numero_1 = input('Digite um número: ')
numero_1f = float(numero_1)

numero_2 = input('Digite um número: ')
numero_2f = float(numero_2)

divisao_inteira = numero_1f // numero_2f
resto_da_divisao = numero_1f % numero_2f
divisao_normal = numero_1f / numero_2f

print('Divisão inteira: ', divisao_inteira ,
'\nResto da divisão: ', resto_da_divisao ,
'\nDivisão normal: ', divisao_normal)