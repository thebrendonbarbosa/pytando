"""
Interpolação básica de strings 
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789) 
"""
nome1 = 'Brendon'
preco = 100.564446546
variavel = '%s, o preço é de R$%.2f' % (nome1,preco)
print(variavel)
print(30*'-')


print('o Hexadecimal de %f é %08X' % (154,154))