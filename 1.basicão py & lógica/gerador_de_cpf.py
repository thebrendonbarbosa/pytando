

import random

nove_digitos =''
for i in range(9):
    nove_digitos += str(random.randint(0,9))


contador_regressivo = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo
    contador_regressivo -= 1

multiplicacao = resultado_digito_1 * 10

resto_1 = multiplicacao % 11

if resto_1 > 9:
    digito_1 = 0
    #print(f'O primeiro dígito do CPF é {digito_1}')
else:
    digito_1 = resto_1
    #print(f'O primeiro dígito do CPF é {digito_1}')

#Segundo dígito

dez_digitos = nove_digitos + str(digito_1)
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
    #print('O segundo dígito do CPF é 0')
else:
    digito_2 = resto_2
   # print(f'O segundo dígito do CPF é {digito_2}')

cpf_gerado_pelo_algoritmo = f'{nove_digitos}{digito_1}{digito_2}'
print(cpf_gerado_pelo_algoritmo)