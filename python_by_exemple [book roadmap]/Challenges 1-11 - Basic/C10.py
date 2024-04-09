"""
010.  There are 2,204 pounds in a kilogram. Ask the
user to enter a weight in kilograms and convert it
to pounds.
"""

peso = input('Informe o peso [Kg]: ')

peso_float = float(peso)
pound_1kg = 2.20462

conversao = peso_float *  pound_1kg

print(f'O valor de {peso_float} [Kg] em Libras é de {conversao} [Lb].')