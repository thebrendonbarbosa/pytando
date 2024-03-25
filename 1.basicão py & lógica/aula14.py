a = 'A'
b = 'B'

c = 1.1

formato = 'a = {}, b = {}, c = {:.2f}'.format(a, b, c)  #:.2f usado para quantizar as casas decimais

print(formato)



#formato por indice
string = 'b = {1} a = {0} a = {0} b = {1} c = {2}'
formato1 = string.format(a, b, c)
print(formato1)



#parametro nomeado
string2 = 'b = {nome2} a = {nome1} a = {nome1} b = {nome2} c = {nome3}'
formato2 = string2.format(
    nome1 = a, nome2= b, nome3 = c)

print(formato2)