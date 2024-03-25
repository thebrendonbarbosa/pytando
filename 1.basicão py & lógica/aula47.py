"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

qts_vezes_tentei = 0

palavra_certa = 'perfume'
letras_acertadas = ''

while True:
    tentativa_letra = input('Digite uma letra: ')
    qts_vezes_tentei += 1

    palavra_apos_tentativa = ''

    if len(tentativa_letra) >1:
        print('Digite apenas uma letra.')
        continue


    if tentativa_letra in palavra_certa:
        letras_acertadas += tentativa_letra 


    for letra_certa in palavra_certa:
        if letra_certa in letras_acertadas:
            palavra_apos_tentativa += letra_certa
        else:
            palavra_apos_tentativa += '*'

    print('Palavra formada:', palavra_apos_tentativa)

    if palavra_apos_tentativa == palavra_certa:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_certa)
        print('Tentativas:', qts_vezes_tentei)
        letras_acertadas = ''
        numero_tentativas = 0
        