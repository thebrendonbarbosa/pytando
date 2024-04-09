"""Create a tuple containing the names of five countries and display the whole tuple. Ask
the user to enter one of the countries that have been shown to them and then display
the index number (i.e. position in the list) of that item in the tuple. """

nomes_paises = ('Arábia Saudita','Guatemala','Israel','Filipinas','Gana')
print(nomes_paises)
escolha_user = input('Escolha um país: ')


print(f'Você escolheu o país {escolha_user}, com índice: ',nomes_paises.index(escolha_user))