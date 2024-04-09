"""
Ask the user to enter 1, 2 or 3. If they enter a 1, display
the message “Thank you”, if they enter a 2, display
“Well done”, if they enter a 3, display “Correct”. If
they enter anything else, display “Error message”.

"""

numero = input('Digite [1], [2], ou [3]: ')
numero_int = int(numero)



if numero_int == 1:
    print('Obrigado!')
elif numero_int == 2:
    print('Muito bem!')
elif numero_int == 3:
    print('Correto!')

else:
    print('Error message.')