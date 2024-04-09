"""Update program 056
so that it tells the 
user if they are too high 
or too low before they 
pick again. """

import random as rd

numero_maquina = rd.randint(1,10)

numero_usuario = int(input('Tente acertar! Digite um número inteiro entre 1 e 10: '))

while numero_usuario != numero_maquina:
    if numero_usuario > numero_maquina:
        print('Muito alto. Você errou! Tente novamente.')
        numero_usuario = int(input('Tente acertar! Digite um número inteiro entre 1 e 10: '))
        continue

    elif numero_usuario < numero_maquina:
        print('Muito baixo. Você errou! Tente novamente.')
        numero_usuario = int(input('Tente acertar! Digite um número inteiro entre 1 e 10: '))
        continue
    
print(f'Parabéns, você acertou! O número era {numero_maquina} e você digitou {numero_usuario}!')