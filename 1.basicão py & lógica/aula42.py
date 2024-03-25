"""
Saber qual a letra aparceu mais na frase

"""

frase = 'Brendo Spbusaaaaaaaaaaaaa' 
#print(frase)

#print(frase.upper().count('P'))
i = 0

qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue


    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes_atual > qtd_apareceu_mais_vezes:
        
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes na frase foi "{letra_apareceu_mais_vezes}", que apareceu {qtd_apareceu_mais_vezes} vezes')

