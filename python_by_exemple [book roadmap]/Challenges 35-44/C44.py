"""Ask how many people the user wants to invite to a party. 
If they enter a number below 10, ask for the names and after 
each name display “[name] has been invited”. If they
enter a number which is 10 or higher, display the message
“Too many people”."""

quantidade_pessoas_festa = input('Quantas pessoas deseja convidar para a festa: ')
quantidade_pessoas_festa_int = int(quantidade_pessoas_festa)

if quantidade_pessoas_festa_int < 10:
    for i in range(0,quantidade_pessoas_festa_int):
        nome = input('Informe o nome do convidado(a): ')
        print(f'{nome} foi convidado!')

elif quantidade_pessoas_festa_int >= 10:
    print('Convidados em excesso.')