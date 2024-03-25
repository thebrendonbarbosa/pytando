"""
Formatação básica de strings
s - strings
d - inteiros
f - float
.<número>f - Quantidade de casas decimais
x ou X - números hexadecimais
(Caracteres)(><^)(Quantidade)(Tipo - s, d, f, x ou X)
> - Esquerda
< - Direita
^ - Centro
Sinal de + - Coloca o sinal de + antes de números positivos
Exemplo: 0>-100,. 1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'

#Criando Padding

print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{variavel:*>10}')
print(f'{1.8967565767:.2f}')
print(f'{1000.36487639288348923:0=+10,.2f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
