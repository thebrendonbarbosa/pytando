"""Make a maths quiz that asks five questions by randomly 
generating two whole numbers to make the question 
(e.g. [num1] + [num2]). Ask the user to enter the 
answer. If they get it right add a point to their score. At 
the end of the quiz, tell them how many they got correct 
out of five. """

import random as rd

pontos = 0

while True:
    qtd_perguntas = 7
    for perguntas in range(qtd_perguntas):
        numero1 = rd.randint(1,9)
        numero2 = rd.randint(1,9)
        resposta_certa = numero1-numero2

        Pergunta = int(input(f'Quanto é {numero1} - {numero2}?  '))
        if Pergunta == resposta_certa:
            pontos += 1

    print(f'Parabéns! Você acertou {pontos} de {qtd_perguntas}!')
    break



