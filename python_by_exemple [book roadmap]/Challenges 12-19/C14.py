"""
014. Ask the user to enter a
number between 10 and 20
(inclusive). If they enter a
number within this range,
display the message “Thank
you”, otherwise display the
message “Incorrect
answer”.
"""


numero = input('Digite um número entre 10 a 20: ')
numero_float = float(numero)

if numero_float >= 10 and numero_float <=20:
    print('Obrigado!')
else:
    print('Resposta errada!')