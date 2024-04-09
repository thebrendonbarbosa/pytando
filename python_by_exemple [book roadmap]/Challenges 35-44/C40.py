"""Ask for a number below 50 and then count down from
50 to that number, making sure you show the number
they entered in the output."""

num = input('Digite um número abaixo de 50: ')
num_int = int(num)

for i in range(0,num_int):
    print('Contagem regressiva: ', 50-i)