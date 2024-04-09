"""
Ask which direction the user wants to count (up or down). 
If they select up, then ask
them for the top number and then count from 1 to that number. 
If they select down, ask
them to enter a number below 20 and then count down from 20 to that number. 
If they entered something other than up or down, display the message 
“I dont understand”."""

direcao = input('Em em sentido voê quer contar? [1-Cima/Baixo] [2-Baixo/Cima]: ')

if direcao == '1': 
    numero_top = input('Digite um número :')
    numero_top_int = int(numero_top)
    for i in range(0, numero_top_int):
        print('Contando de Cima/Baixo: ', numero_top_int - i)

elif direcao == '2':
    numero_inicio = input('Digite um número abaixo de 20:')
    numero_inicio_int = int(numero_inicio)
    for i in range(0, numero_inicio_int):
        print('Contando de Baixo/Cima: ', i)

else:
    print('Eu não entendi!')
