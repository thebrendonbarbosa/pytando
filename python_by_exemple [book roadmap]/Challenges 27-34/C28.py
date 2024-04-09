"""
Update program 027 so that it will display the answer to
two decimal places.
"""


num = input('Digite um número: ')
num_float = float(num)

multiplicacao = num_float * 2

print(f'O resultado é: {multiplicacao:.2f}')