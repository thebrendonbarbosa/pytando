"""
Ask the user to enter their
name and a number. If the
number is less than 10, then
display their name that
number of times; otherwise
display the message “Too
high” three times.
"""
nome = input('Digite seu nome: ')
numero = input('Digite um número: ')
int_numero = int(numero)

if int_numero < 10:
    for i in range(0, int_numero):
        print(nome)
else: 
    print('Número muito alto!')