# Manipulando chaves e valores em dicionários

pessoa = {}


# adiciona um chave e valor
pessoa['nome'] = 'Thalyson'

#print(pessoa)

# chaves dinamicas
chave = 'sobrenome'
pessoa[chave] = 'Silva'


# alterar o valor das chaves
pessoa[chave] = 'Soares'
#print(pessoa[chave])

# Apagar chaves
del pessoa['nome']
print(pessoa)

# acessando chave
print(pessoa[chave])

# saber se 1 chave existe em 1 dict
print(pessoa.get('nome'))
print(pessoa.get('sobrenome'))

if pessoa.get('nome') is None:
    print('Não existe')
else: 
    print(pessoa['nome'])