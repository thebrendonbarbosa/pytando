""""
while/else
"""
"""
toda vez que o laço while é executado até o fim o else é execuado
"""

string = 'ValorA'

i = 0
while i< len(string):
    letra = string[i]


    """
    fazer o prog nao chegar no else é colcoar um break quando atingir o que eu quero
    """
    if letra == ' ':
        break

    print(letra)
    i += 1

else:
    print('Não encontrei espaço na string / O else foi executado.')
print('Fora do while')