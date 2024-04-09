"""Add to program 069 to ask the
user to enter a number and
display the country in that
position. 
"""


nomes_paises = ('Arábia Saudita','Guatemala','Israel','Filipinas','Gana')
print(nomes_paises)
escolha_user = input('Escolha um número: ')
escolha_user_int = int(escolha_user)

print(f'Você escolheu o número {escolha_user_int} que corresponde ao país {nomes_paises[escolha_user_int]}.')
