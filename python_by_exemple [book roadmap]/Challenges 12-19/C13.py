"""
013 .Ask the user to enter a
number that is under
20. If they enter a
number that is 20 or
more, display the
message “Too high”,
otherwise display
“Thank you”.
"""

numero= input('Digite um número menor ou igual a 20: ')
numero_float = float(numero)

if numero_float >= 20:
    print('Número digitado muito alto.')

else:
    print('Valeu,cara!') 