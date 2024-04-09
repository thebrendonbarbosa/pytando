"""
Ask the user to enter a
number and then enter
another number. Add these
two numbers together and
then ask if they want to add
another number. If they
enter “y", ask them to enter
another number and keep
adding numbers until they
do not answer “y”. Once the
loop has stopped, display
the total."""

numero_1 = float(input('Digite um número: '))
numero_2 = float(input('Digite outro número: '))

total_1 = numero_1 + numero_2
total = total_1
adicionar = input('Deseja adicionar mais um número?  ')

while adicionar == 'y':
    numero = float(input('Digite um número: '))
    total += numero
    adicionar = input('Deseja adicionar mais um número?  ')
    continue
print(f'A soma dos números informados é de {total}')