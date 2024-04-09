"""Escolha aleatoriamente cara ou coroa ("K" ou "C"). Pedir 
o usuário para fazer sua escolha. Se a escolha for a mesma 
como o valor selecionado aleatoriamente, exiba a mensagem 
"Você ganha", caso contrário, exiba "Azar". No final, conte 
o usuário se o computador selecionou cara ou coroa. """

import random as rd

resultados = ['K', 'C']
resultado_maquina = rd.choice(resultados)

entrada_usuario = input('Escolha Cara [K] ou Coroa [C]: ') 

if entrada_usuario == resultado_maquina:
    print(f'Você ganhou! O resultado era {resultado_maquina}.')
else:
    print(f'Você errou! O resultado era {resultado_maquina}.')