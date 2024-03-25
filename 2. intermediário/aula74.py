# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

numero = float(input('Digite um número: '))



def duplicar(numero):
    return numero*2
    
def triplicar(numero):
    return numero*3
    
def quadruplicar(numero):
    return numero*4


dobro = duplicar(numero)
triplo = triplicar(numero)
quadruplo = quadruplicar(numero)



print(f'O dobro do número {numero} é {dobro}!')
print(f'O triplo do número {numero} é {triplo}!')
print(f'O quadruplo do número {numero} é {quadruplo}!')