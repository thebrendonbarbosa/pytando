""" Exercícios com funções
Crie uma função que multiplica todos os argumentos não nomeados recebidos 
Retorne o total para uma variável e mostre o valor
da variável.
"""

def multipli_valores(*args):
    total = 1
    for numero in args:
        total = total*numero
    return total

resultado = multipli_valores(1,2,5) 
print(resultado)

"""
Crie uma função fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar."""

def parimpar(x):
    if x%2 == 0:
        print(f'O número {x} é par!')
    else:
        print(f'O número {x} é impar!') 
parimpar(4)