"""Create a list of four three-digit
numbers. Display the list to the
user, showing each item from
the list on a separate line. Ask
the user to enter a three-digit
number. If the number they
have typed in matches one in
the list, display the position of
that number in the list,
otherwise display the message
“That is not in the list”. """

lista = [
    123, 456, 789, 401
]

#for i in range(len(lista)):
#    print(lista[i])
lista_enumerada = enumerate(lista) 
for indice, valor in lista_enumerada:
    print(indice,valor)
numero_usuario = input('Digite uma sequencia de tres números: ')
numero_usuario_int = int(numero_usuario)

if numero_usuario_int in lista:
    print('O numero que vc digitou está na lista! O indice é: ')
    print(lista.index(numero_usuario_int))
else:
    print('Esse valor não está na lista.')