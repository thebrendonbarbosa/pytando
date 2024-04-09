"""
Ask the user to enter a
number with lots of
decimal places. Multiply
this number by two and
display the answer.
"""


num = input('Digite um número: ')
num_float = float(num)

multiplicacao = num_float * 2

print(f'O resultado é:{multiplicacao}')