# Operadores in e not in 
# Strings são iteráveis
#  0 1 2 3 4 5 6
#  b r e n d o n
# -7-6-5-4-3-2-1

nome = 'brendon'

print(nome[0])
print(nome[-7])

print('d' in nome) # confere se a string está entre o nomeC 
print('s' in nome)
print('ren' in nome)
print(10*'-')
print('bre' not in nome)

print(25*'*')

nome = input('Digite um nome: ')
encontrar = input('Digite a sílaba ou letra que deseja encontrar no nome: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')