"""Alter program 035 so that it will ask the user to enter their
name and a number and then display their name that
number of times."""

nome = input('Digite seu nome: ')
vezes = input('Quantas vezes quer imprimir seu nome? ')
vezes_int = int(vezes)

for i in range(0,vezes_int):
    print(nome)