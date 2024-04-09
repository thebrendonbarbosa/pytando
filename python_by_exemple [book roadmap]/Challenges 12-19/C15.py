"""
015. Ask the user to enter their favourite colour. If they enter “red”, “RED” or
“Red” display the message “I like red too”, otherwise display the message
“I dont like [colour], I prefer red”.

"""

cor = input('Qual é a sua cor favorita? ')

cor_aceitacel = ' Vermelho, VERMELHO, vermelho'

if cor in cor_aceitacel:
    print(f'Eu gosto de {cor} também!')
else:
    print(f'Eu não gosto de {cor}!')