"""
https://docs.python.org/pt-br/3/library/stdtypes.html

Imutáveis que vimos = int, float, string,bool

"""

string = 'Brendin Barsi'

string[2]

# Não 'epossivel mudar o valor de string[2]
#string[2] = 's'


#forma da mudança

outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)

#Os tipos apresentados são objetos
#Posso fazer ações com eles

print(string.capitalize())
print(string.zfill(40))