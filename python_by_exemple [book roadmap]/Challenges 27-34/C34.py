"""
Display the following message:
1)square
2)triangule
Enter a number: 
If the user enters 1, then it should ask them for
the length of one of its sides and display the
area. If they select 2, it should ask for the base
and height of the triangle and display the area. If
they type in anything else, it should give them a
suitable error message.

"""
import math

mensagem_inicio = input('[1] Quadrado\n'
                        '[2] Triangulo\n'
                        'Digite um número: ' )

numero_mensagem = int(mensagem_inicio)

if numero_mensagem == 1:
    comprimento_quadrado = input('Informe o comprimento de um dos lados do quadrado em metros: ')
    comprimento_quadrado_f = float(comprimento_quadrado)
    area_quadrado = comprimento_quadrado_f **2
    print(f'A área de um dos lados do quadrado é {area_quadrado:.2f} metros quadrados')

elif numero_mensagem == 2: 
    base_triangulo = input('Informe a comprimento da base do triângulo em metros: ')
    base_triangulo_f = float(base_triangulo)
    altura_triangulo = input('Informe a altura da base do triângulo em metros: ')
    altura_triangulo_f = float(altura_triangulo)
    area_triangulo = (base_triangulo_f*altura_triangulo_f)/ 2
    print(f'A área total do triângulo é {area_triangulo:.2f} metros quadrados. ')

else:
    print('Opção inválida!')