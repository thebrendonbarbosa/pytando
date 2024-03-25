
"""
Repetições
While - enquanto algo for verdadeiro
For - para cada elemento de uma sequência
Loop infinito - while True - quando não temos uma condição de parada
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Pulei o seis')
        continue

    if contador >= 10 and contador <=27:
        print('Pulei o',contador)
        continue

    print(contador)

    if contador == 50:
        break
print('Acabou')