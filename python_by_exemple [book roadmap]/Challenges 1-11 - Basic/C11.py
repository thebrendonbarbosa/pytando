"""
011. Task the user to enter a number over 100 and then enter a number under
10 and tell them how many times the smaller number goes into the larger
number in a user-friendly format.
"""


numero_1 = input('Digite um número maior que 100: ')
numero_2 = input('Digite um número menor que 10: ')

numero_1_int = int(numero_1)
numero_2_int = int(numero_2)

divisao = numero_1_int/numero_2_int

print(f'O número {numero_2_int} cabe no número {numero_1_int} {divisao} vezes.')