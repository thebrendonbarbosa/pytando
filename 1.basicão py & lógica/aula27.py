"""
Fatiamento de strings
    0123456789
    Olá mundo
  -10987654321
Fatiamento [inicio:fim:passo] [::]
Obs: a função len retorna a quantidade de caracteres da str

"""
variavel = 'Ola mundo!'

print(variavel[1])
print(variavel[1:])
print(variavel[::2])
print(variavel[1:3])
print(variavel[0:10:2])
print(variavel[-9])
print(variavel[::-1])
print(variavel[-1:-4:-1])