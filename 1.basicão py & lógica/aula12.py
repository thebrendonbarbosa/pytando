#Exercício de programação - Cálculo do IMC (Índice de Massa Corpórea) + Ellipsis

nome = str(input('Qual seu nome? '))
altura = float(input('Qual sua altura em metros? '))
peso = float(input('Qual seu peso em Kg? '))
imc = peso/ (altura)**2


if imc>= 40:
    print(nome,'seu imc é:', imc, 'você está com obesidade morbida!')
else:
    print(nome,'seu imc é:', imc)