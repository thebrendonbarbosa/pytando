##CAlculo imc 
from math import *

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
altura = input('Digite sua altura: ')
peso = input('Digite seu peso: ')

idade_int = int(idade)
altura_float = float(altura)
peso_float= float(peso)


imc = peso_float/altura_float**2

if imc < 18.5:
    print(f'{nome}, seu IMC é de {imc:.2f} e você está abaixo do peso.')
elif imc >= 18.5 and imc < 24.9:
    print(f'{nome}, seu IMC é de {imc:.2f} e seu peso está normal.')
elif imc >= 24.9 and imc <=29.9:
    print(f'{nome}, seu IMC é de {imc:.2f} e você está com sobrepeso.')
elif imc >=30.0 and imc <= 34.9:
    print(f'{nome}, seu IMC é de {imc:.2f} e você está com Obesidade grau I.')
elif imc >=35 and imc <=39.9:
    print(f'{nome}, seu IMC é de {imc:.2f} e vocÊ está com Obesidade grau II.')
elif imc >=40:
    print(f'{nome}, seu IMC é de {imc:.2f} e você está com Obesiade mórbida.')


