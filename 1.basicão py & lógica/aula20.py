"""
Exercício - Faça um programa 
para checar se um valor é maior que o outro
"""

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que {segundo_valor=}!')
elif primeiro_valor < segundo_valor:
    print('O segundo valor é maior que o primeiro valor')
elif primeiro_valor == segundo_valor:
    print('Os valores são iguais!')