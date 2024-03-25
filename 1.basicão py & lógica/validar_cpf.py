"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import re 
import sys


entrada = input('Informe o CPF (Somente números): ')

cpf_digitado = re.sub(r'[^0-9]','',entrada )


entrada_e_sequencial = entrada == entrada[0]* len(entrada)
if entrada_e_sequencial:
    print('você enviou dados sequenciais.')
    sys.exit()   #MAta o programa aqui

nove_digitos = cpf_digitado[:9]
contador_regressivo = 10

resultado = 0
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1

multiplicacao = resultado * 10

resto_1 = multiplicacao % 11

if resto_1 > 9:
    digito_1 = 0
    print(f'O primeiro dígito do CPF é {digito_1}')
else:
    digito_1 = resto_1
    print(f'O primeiro dígito do CPF é {digito_1}')

#Segundo dígito

dez_digitos = cpf_digitado[:10]
contador_regressivo_2 = 11

resultado_2 = 0
for digito_2 in dez_digitos:
    resultado_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
#print(resultado)

multiplicacao_2 = resultado_2 * 10

resto_2 = multiplicacao_2 % 11

if resto_2 > 9:
    digito_2 = 0
    print('O segundo dígito do CPF é 0')
else:
    digito_2 = resto_2
    print(f'O segundo dígito do CPF é {digito_2}')

cpf_gerado_pelo_algoritmo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_digitado == cpf_gerado_pelo_algoritmo:
    print(f'{cpf_gerado_pelo_algoritmo} é válido!')
else:
    print('CPF inválido.')