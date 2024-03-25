# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados tipo par de "Chaves" e "Valor"
# Chaves podem ser consideradas como o "indice" das listas e podem ser de tipos imutáveis
# O valor pode ser de qualquer tipo, incluindo outro dicionario
# Usamos as chaves - {} - ou a classe dict para criar dicionários
# Imutáveis: str, int, float, bool, tuple
# Mutáveis: dict, list

pessoa = {
    'nome': 'Brendon Barbosa',
    'sobrenome': 'Silva',
    'idade': 18,
    'endereços': [
        {'rua': 'Santa X', 'número': 144},
        {'rua': 'Agt S', 'número': 44 },
        ],
}

# outra forma de fazer
pessoa_2 = dict(nome='Maria', sobrenome = 'Silva') 

#print(pessoa,pessoa_2)
print(pessoa['endereços'])