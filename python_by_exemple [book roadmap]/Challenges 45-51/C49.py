"""49 - Create a variable called
compnum and set the value
to 50. Ask the user to enter a
number. While their guess
is not the same as the
compnum value, tell them if
their guess is too low or too
high and ask them to have
another guess. If they enter
the same value as
compnum, display the
message “Well done, you
took [count] attempts”."""

numero_do_computador = 50

numero = input('Adivinhe o número! Digite um número: ')
numero_int = int(numero)
contador_de_tentativas =1

while numero_int != numero_do_computador:
    
    diferenca = numero_do_computador - numero_int

    if diferenca > 0:
        print('Numero muito baixo!')
    elif diferenca < 0:
        print('Número muito alto!')
    
    numero = input('Adivinhe o número! Digite um número: ')
    numero_int = int(numero)
    contador_de_tentativas += 1
    continue

print(f'Muito bem! Você acertou aṕos {contador_de_tentativas} tentaivas! O número era {numero_do_computador}!')