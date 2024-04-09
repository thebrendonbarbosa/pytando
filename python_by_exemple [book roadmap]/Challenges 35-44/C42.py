"""
Set a variable called total to 0. Ask the user to enter
five numbers and after each input ask them if they
want that number included. If they do, then add the
number to the total. If they do not want it included,
dont add it to the total. After they have entered all five
numbers, display the total."""

total = 0

for i in range(0,5):
    num = input('Digite um número: ')
    num_int = int(num)
    Adicionar = input('Deseja adicionar este número ao total? [S] ou [N]: ')
    if 'S' in Adicionar:
        total = total + num_int
        print(f'A soma total atual é de {total}')
    else:
        total = total
        print(f'A soma total atual é de {total}')

print(f' A soma total dos números é de {total}')