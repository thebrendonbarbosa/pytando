"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Função soma
def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')


#Funcão subtração
def subtracao(n,m,p):
    print(n-m-p)

subtracao(0,11,-4)

#Função multoplicacao
def multiplicacao(a,b):
    print(f'A multiplicação de dois números, a = {a} e b = {b} é igual a {a*b}.')
multiplicacao(4,7)