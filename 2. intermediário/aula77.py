# Métodos úteis dos dics

pessoa = {
    'nome': 'Brendon Barbosa',
    'sobrenome': 'Silva',
    'idade': 18,
    'endereços': 'Rua X, 14',
}

# len - quanatidade de chaves
print(len(pessoa))


# keys -retornar as chaves - iterável com as chaves
print(pessoa.keys())
print(list(pessoa.keys()))


# values - iterável com os valores
print(pessoa.values())

# items - iteravel com chaves e valores
print(pessoa.items())
print(list(pessoa.items()))

print('__________________________')
for chave,valor in pessoa.items():
    print(chave,valor)

# setdefault - adiciona valor se a chave não existe
"""Seta um valor padrão se a chave nao existir no dict, se a cahve existir nao da em nada"""
pessoa.setdefault('Cor', 'Preta')
print(pessoa['Cor'])

