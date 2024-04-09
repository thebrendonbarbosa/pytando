"""
Ask the user to enter the radius of a circle
(measurement from the centre point to the edge). Work
out the area of the circle (π*radius2).
"""

import math

raio = input('Informe o raio do circulo em metros: ')
raio_f = float(raio)

area = math.pi * raio_f**2

print(f'A área do círculo de {area:.4f} metros.')