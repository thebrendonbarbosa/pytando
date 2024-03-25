#Formatando Strings com F strings

nome = str(input('Qual seu nome? '))
altura = float(input('Qual sua altura em metros? '))
peso = float(input('Qual seu peso em Kg? '))
imc = peso/ (altura)**2

linha_1 = f'{nome} ,seu imc é:{imc:.2f} você está com obesidade morbida!'
linha_2 = f'{nome}, seu imc é: {imc:.2f}!'

if imc>= 40:
    print(linha_1)
else:
    print(linha_2)