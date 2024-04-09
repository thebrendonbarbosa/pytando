"""
Ask the user to enter a number. If it is under 10,
display the message “Too low”, if their number is
between 10 and 20, display “Correct”, otherwise
display “Too high”.

"""

numero = input('Digite um número: ')
numero_float = float(numero)

if numero_float < 10:
    print('Muito baixo!')

elif numero_float >= 10 and numero_float <= 20:
    print('Resposta certa!')

else:
    print('Muito alto!')


