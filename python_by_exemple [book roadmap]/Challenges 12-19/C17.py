"""
017. Ask the users age. If they
are 18 or over, display the
message “You can vote”, if
they are aged 17, display the
message “You can learn to
drive”, if they are 16, display
the message “You can buy a
lottery ticket”, if they are
under 16, display the
message “You can go Trick-
or-Treating”.
"""

idade = input('Qual é a sua idade? ')
idade_int = int(idade)

if idade_int >= 18:
    print('Você pode votar!')

if idade_int == 17:
    print('Você pode aprender a dirigir!')

if idade_int == 16:
    print('Você pode comprar um bilhete de loteria.')

else:
    print('Você pode ir fazer Trick-or-Treating.')