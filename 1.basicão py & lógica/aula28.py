"""
Introdução ao Try/ Except
Try -> Tentar executar o código
except > Ocorreu algum erro ao tentar executar

"""

# Erro 1
#print(123)
#print(456)
#int('s') # Retorna uma Exceçaõ (erro - ValueError)

numero_str = input('Digite um número. Vou dobrar o valor!')


try:
    #print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')