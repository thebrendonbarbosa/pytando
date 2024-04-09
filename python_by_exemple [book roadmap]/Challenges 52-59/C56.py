"""Randomly pick a whole number between 1 
and 10. Ask the user to enter a number and 
keep entering numbers until they enter the 
number that was randomly picked. """

import random as rd

numero_maquina = rd.randint(1,10)

numero_usuario = int(input('Tente acertar! Digite um número inteiro entre 1 e 10: '))

while numero_usuario != numero_maquina:
    print('Você errou! Tente novamente.')
    numero_usuario = int(input('Tente acertar! Digite um número inteiro entre 1 e 10: '))
    continue

print(f'Parabéns, você acertou! O número era {numero_maquina} e você digitou {numero_usuario}!')