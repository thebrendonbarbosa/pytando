"""Ask the user to enter a number between 1
and 12 and then display the times table for
that number."""


numero = input('Digite um número entre 1 e 12: ')
numero_int = int(numero)

for i in range(0,10):
    print(numero_int*i)