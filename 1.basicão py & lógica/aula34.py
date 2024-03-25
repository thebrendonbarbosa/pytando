"""
Repetições
While - enquanto algo for verdadeiro
For - para cada elemento de uma sequência
Loop infinito - while True - quando não temos uma condição de parada
"""
Condicao = True

while Condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é {nome}')
    if nome == 'Sair':
        break
print('Acabou')