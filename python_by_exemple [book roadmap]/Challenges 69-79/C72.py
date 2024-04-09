"""Create a list of six school subjects. Ask the user which of these
subjects they dont like. Delete the subject they have chosen from the
list before you display the list again"""

objetos_escola = ['Quadro negro', 'Caderno','Lápis', 'Cadeira', 'Apagador', 'Borracha']
print(objetos_escola)
print(50*'*')
objeto_user_nao_gosta = input('Dentre os itens da lista acima, qual objeto você não gosta: ')

objetos_escola.remove(objeto_user_nao_gosta)

print('Certo, o item o removido com sucesso!')
print(objetos_escola)