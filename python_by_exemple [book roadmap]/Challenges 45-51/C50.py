"""
Ask the user to enter a number between
10 and 20. If they enter a value under 10,
display the message “Too low” and ask
them to try again. If they enter a value
above 20, display the message “Too high”
and ask them to try again. Keep repeating
this until they enter a value that is
between 10 and 20 and then display the
message “Thank you”
"""

numero_usuario = input('Digite um número entre 10 e 20: ')
numero_usuario_float = float(numero_usuario)

contador_de_tentativas = 1

while numero_usuario_float >20 or numero_usuario_float <10:
    if numero_usuario_float < 10:
        print('Número muito baixo!')
    elif numero_usuario_float > 20:
        print('Número muito alto!')

    contador_de_tentativas += 1
    numero_usuario = input('Digite um número entre 10 e 20: ')
    numero_usuario_float = float(numero_usuario)
    continue
print(f'Obrigado, Nº de tentativas: {contador_de_tentativas}')