# Métodos úteis dos dics
import copy

# # copy - retorna uma cópia rasa (shallow copy)
d1 = {
    'chave1': 1,
    'chave2': 2,
    'lista1': [0, 1, 2]
}

d2 = d1.copy() # nao altera o valor de d1 de dados imutaveis
#d2 = copy.copy(d1)
d3 = copy.deepcopy(d1) 

d2['chave1']= 1000
d2['lista1'][1] = 7777
print(d1)
print(d2)
print(d3)

# get - obtem uma chave
p1 = {
    'nome': 'Luiz',
    'altura': 1.88,
    'idade': 44
}

print(p1.get('nome'))
print(p1.get('sobrenome', 'Não existe'))


# pop - apaga um item com a chave especificada(del)
nome = p1.pop('nome')
print(nome)
print(p1)

# popitem - apaga o ultimo item adicionado
ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)


#update - atualiza um dicionario com outro
p1.update({
    'altura': 1.66,
    'filhos': 0,
    'peso': 88
})
# p1.update(altura=1.66, filhos=0, peso=88)

# tupla = ('nome', 'novo valor'),('idade', 30)
# lista = [['nome', 'novo valor'],['idade', 30]]
#p1.update(tupla)
#p1.update(lista)
print(p1)