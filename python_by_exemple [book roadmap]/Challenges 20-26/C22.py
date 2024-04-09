"""
022. Ask the user to enter their first name and surname in lower
case. Change the case to title case and join them together.
Display the finished result.
"""

nome = input('Informe seu nome em letras minúsculas: ')
sobrenome = input('Informe seu sobrenome em letras minúsculas: ')

nome_completo = nome +' '+ sobrenome

print(f'Olá, {nome_completo.title()}!')