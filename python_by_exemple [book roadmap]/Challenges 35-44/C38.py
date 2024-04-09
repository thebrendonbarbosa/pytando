"""Change program
037 to also ask for a
number. Display
their name (one
letter at a time on
each line) and
repeat this for the
number of times
they entered."""

nome = input('Digite seu nome: ')
numero = input('Digite um número: ')
numero_int = int(numero)

for l in range(0,numero_int):
    for i in nome:
        print(i)