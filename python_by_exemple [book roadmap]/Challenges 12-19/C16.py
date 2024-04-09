"""
016. Ask the user if it is raining and convert their answer to lower case
so it doesnt matter what case they type it in. If they answer “yes”,
ask if it is windy. If they answer “yes” to this second question,
display the answer “It is too windy for an umbrella”, otherwise
display the message “Take an umbrella”. If they did not answer yes
to the first question, display the answer “Enjoy your day”. 

"""

pergunta1 = input('Está chovendo? ').lower()



if pergunta1 == 'sim':

    pergunta2 = input('Está ventando? ').lower()

    if pergunta2 == 'sim':
        print('Está ventando demais para usar o guarda-chuva.')
    else:
        print('Use um guarda-chuva.')


else:
    print('Aproveite seu dia!')
