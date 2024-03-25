
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def enumera_lista():
    
    numero_apareceu_mais_vezes = 0

    lista_enumerada = enumerate(lista_de_listas_de_inteiros)
    i = 0
    qtd_apareceu_mais_vezes=0
    while i < len(lista_de_listas_de_inteiros):
        for indice,valor in lista_enumerada:
            numero_atual = valor[i]

            print(numero_atual)
            if numero_atual == ' ':
                i += 1
                continue
            qtd_apareceu_mais_vezes_atual = lista_de_listas_de_inteiros.count(numero_atual)
            if qtd_apareceu_mais_vezes_atual > qtd_apareceu_mais_vezes:
                qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
                numero_apareceu_mais_vezes = numero_atual
                
            i += 1
    return

enumera_lista()
