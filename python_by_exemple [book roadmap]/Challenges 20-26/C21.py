"""
021. Ask the user to enter their first name and then ask them to
enter their surname. Join them together with a space between
and display the name and the length of whole name.

"""

nome = input('Qual o seu primeiro nome? ')
sobrenome = input('Qual é o seu sobrenome? ')

nome_completo = nome +' '+sobrenome

print(f'Olá, {nome_completo}.')