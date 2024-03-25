"""
Repetições
While - enquanto algo for verdadeiro
For - para cada elemento de uma sequência
Loop infinito - while True - quando não temos uma condição de parada
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna =1
    while coluna <= qtd_colunas:
        print(f'{linha=}{coluna=}')
        coluna += 1
    linha += 1

print('Acabou')