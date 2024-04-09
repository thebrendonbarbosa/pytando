"""Enter a list of ten colours.
Ask the user for a starting
number between 0 and 4
and an end number
between 5 and 9. Display
the list for those colours
between the start and end
numbers the user input. """

cores = [
    'Azul','Amarelo','Cinza','Branco', 'Laranja', 'Marrom','Preto', 'Vermelho','Verde', 'Ciano'
    ]

numero_inicio = input('Digite um número inicial entre 0 e 4: ')
numero_inicio_int = int(numero_inicio)

numero_final = input('Digite um número final entre 5 e 9: ')
numero_final_int = int(numero_final)

print(cores[numero_inicio_int:numero_final_int])

