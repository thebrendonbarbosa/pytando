"""
025. Ask the user to enter their first name. If the length
of their first name is under five characters, ask
them to enter their surname and join them
together (without a space) and display the name
in upper case. If the length of the first name is five
or more characters, display their first name in
lower case.

"""

nome = input('Informe seu nome: ')


if len(nome) < 5:
    sobrenome = input('Informe seu sobrenome: ')
    nome_junto = nome+sobrenome 
    print(nome_junto.upper())
else:
    print(nome.lower())
