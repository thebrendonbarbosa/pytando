"""
008.  Ask for the total price of the bill, then ask how
many diners there are. Divide the total bill by the
number of diners and show how much each
person must pay.
"""


total_bill = input('Informe o total da conta: ')

pessoas = input('Quantas pessoas jantaram? ')

total_bill_float = float(total_bill)
pessoas_int = int(pessoas)

valor_dividido = total_bill_float/ pessoas_int

print(f'Cada pessoa deve pagar R$:{valor_dividido}.')