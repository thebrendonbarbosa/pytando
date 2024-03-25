"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Programa 1 - Minha resposta

numero_str = input('Digite um número inteiro: ')

try:
    numero_int = int(numero_str)
    modulo = numero_int % 2
    if modulo == 0:
        print('Seu número é par!')
    else:
        print('Seu número é impar!')
except:
    print('Isso não é um número inteiro!')

# Programa 1 - Resoluçao professor

entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int %2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro!')

# Programa 2

hora = input('Informe a hora: ')

manha_inicio = 0
manha_fim = 11
tarde_inicio = 12.00
tarde_fim = 17
noite_inicio = 18
noite_fim = 23

try:
    hora_int = int(hora)
    if hora_int >= manha_inicio and hora_int <= manha_fim:
        print(f'São {hora_int} horas. Bom dia!')

    elif hora_int >= tarde_inicio and hora_int <= tarde_fim:
        print(f'São {hora_int} horas. Boa Tarde!')

    elif hora_int >= noite_inicio  and hora_int <= noite_fim:
        print(f'São {hora_int} horas. Boa Noite!')

except:
    print('Horário incorreto.')



# Programa 3

nome_usuario = input('Digite seu nome: ')

tamanho_nome = len(nome_usuario)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto.')

    elif tamanho_nome >= 5 and tamanho_nome <=6:
        print('Seu nome tem o tamanho normal.')

    else:
        print('Seu nome é grande.')
else:
    print('Digite mais de uma letra.')