"""Ask the user to enter
a number. Keep
asking until they enter
a value over 5 and
then display the
message “The last
number you entered
was a [number]” and
stop the program."""


numero = input("Digite um número: ")
numero_float = float(numero)

while numero_float <=5:
    print('Valor baixo de 5.')
    numero = input('Digite um número: ')
    numero_float = float(numero)
    continue
print(f'Seu último número foi {numero_float}')