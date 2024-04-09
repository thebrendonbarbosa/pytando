"""
023. Ask the user to type in the first
line of a nursery rhyme and
display the length of the string.
Ask for a starting number and an
ending number and then display
just that section of the text
(remember Python starts
counting from 0 and not 1).
"""

cancao = input('Informe um trecho de uma canção de ninar: ')
print(f'O tamanho do trecho é {len(cancao)}')

inicio = int(input('Informe um número inicial: '))
fim = int(input('Informe um número final: '))

print(cancao[inicio:fim])