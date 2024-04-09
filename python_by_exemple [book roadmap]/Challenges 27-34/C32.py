"""
Ask for the radius and the depth of a cylinder
and work out the total volume (circle
area*depth) rounded to three decimal
places.
"""
import math

raio = input('Informe o raio do cilindro em metros: ')
raio_f = float(raio)

profundidade = input('Informe a profundidade do cilindro em metros: ')
profundidade_f = float(profundidade)

area = math.pi * raio_f**2
volume = area * profundidade_f

print(f'O volume do cilindro é {volume:.3f} metros cúbicos.')