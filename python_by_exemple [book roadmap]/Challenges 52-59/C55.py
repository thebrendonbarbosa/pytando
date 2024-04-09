"""Randomly choose a number between 1 and 5. Ask the user to pick a 
number. If they guess correctly, display the message “Well done”, 
otherwise tell them if they are too high or too low and ask them to pick a 
second number. If they guess correctly on their second guess, display 
“Correct”, otherwise display “You lose”."""

import random as rd

numero_maquina = rd.randint(1,5)

numero_usuario = int(input('Tente acertar! Escolha um número entre 1 e 5: '))
if numero_usuario == numero_maquina:
    print('Você acertou!')

elif numero_usuario > numero_maquina:
    print("Muito alto!")
    numero_usuario2 = int(input('Escolha novamente um número entre 1 e 5: '))
    if numero_usuario2 == numero_maquina:
        print('Você acertou!')
    else:
        print(f'Você errou! O número era {numero_maquina}.')

elif numero_usuario < numero_maquina:
    print("Muito baixo!")
    numero_usuario3 = int(input('Escolha novamente um número entre 1 e 5: '))

    if numero_usuario3 == numero_maquina:
        print('Você acertou!')
    else:
        print(f'Você errou! O número era {numero_maquina}.')