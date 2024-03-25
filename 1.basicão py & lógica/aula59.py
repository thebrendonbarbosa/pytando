"""
Split e join com list e str
split - divide uma string
join - une uma string

strip- corta os espaços vazios da frase
      rstrip - corta do lado direito
      lstrip - corta do lado esquerdo
"""

frase = "Olha só que coisa legal"

#Separa a frase pelos espaços
lista_palavras = frase.split()
print(lista_palavras)


#Serando pelo o que eu quiser no arguemnto de split
frase2 = "    Eu vou,    nós vamos,    eles vão "
lista_palavras2_cruas = frase2.split(',')
lista_frases = []
for i, frase in enumerate(lista_palavras2_cruas):
    lista_frases.append(lista_palavras2_cruas[i].strip())


print(lista_palavras2_cruas)
print(lista_frases)


# UNINDO FRASES
frases_unidas = '*'.join('abc')
print(frases_unidas)

frases_unidas2 = '-'.join(lista_frases)
print(frases_unidas2)