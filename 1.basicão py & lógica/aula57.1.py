"""
Exercicio - Crie um alista de compras
O usuario deve ter a possibilidade de inserir,apagar e listar
valores da sua lista de compras
não permita que o programa quebre com os erros de indice
inexistentes na lista.

"""

lista_de_compras = []


while True:

    opcao_inicial = input('-----------------------\nLISTA DE COMPRAS\nSelecione uma opção:\n [i] Inserir | [a] Apagar | [l] Listar: ')
    respostas_validas = ('a', 'i', 'l')

    if opcao_inicial not in respostas_validas:
       print('Erro. Digite uma opão válida.')
       continue
    
    if opcao_inicial == 'i':
        valor_novo = input('Informe o valor:')
        lista_de_compras.append(valor_novo)
        continue

    if opcao_inicial == 'a':
        item_apagar = input('Informe o intem que deseja apagar: ')
        item_apagar_int = int(item_apagar)
        if item_apagar_int > len(lista_de_compras) or item_apagar_int<0:
            print('Item não encontrado.')
        else:
            del lista_de_compras[item_apagar_int]
        continue

    if opcao_inicial == 'l':
        if len(lista_de_compras) == 0:
            print('Não há nada para exibir')
        else:
            for item, valor in enumerate(lista_de_compras):
                print(item, valor)
        continue

    