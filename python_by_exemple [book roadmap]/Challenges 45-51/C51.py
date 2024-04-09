""""
Using the song “10 green bottles”, display the lines “There are [num] green bottles
hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle
should accidentally fall”. Then ask the question “how many green bottles will be
hanging on the wall?” If the user answers correctly, display the message “There will be
[num] green bottles hanging on the wall”. If they answer incorrectly, display the
message “No, try again” until they get it right. When the number of green bottles gets
down to 0, display the message “There are no more green bottles hanging on the wall”."""


numero_garrafas_verdes = 9

verso1 = f'Há {numero_garrafas_verdes+1} garrafas verdes penduradas na parede, {numero_garrafas_verdes+1} verdes ' \
'garrafas penduradas na parede, e se 1 garrafa verde cair acidentalmente.'

print(verso1)
pergunta_usuario = int(input('Quantas garrafas verdes estarão penduradas na parede? ' ))

while numero_garrafas_verdes !=  0:
    
    if pergunta_usuario == numero_garrafas_verdes:
        print(f'Haverá {numero_garrafas_verdes} garrafas verdes penduradas na parede')
        numero_garrafas_verdes -= 1
        pergunta_usuario = int(input('Quantas garrafas verdes estarão penduradas na parede? ' ))
        continue
    else:
        print('Errado! Tente novamente!')
        pergunta_usuario = int(input('Quantas garrafas verdes estarão penduradas na parede? ' ))
        continue
    
print('Não há mais garrafas verdes penduradas na parede')

