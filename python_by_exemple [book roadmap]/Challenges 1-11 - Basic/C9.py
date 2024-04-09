"""
009.  Write a program that will ask for a
number of days and then will
show how many hours, minutes
and seconds are in that number of
days.
"""

day = input('Informe o número de dias: ')
day_int = int(day)

horas_do_dia = day_int* 24
minutos_do_dia = horas_do_dia *  60
segundos_do_dia = minutos_do_dia * 60

print(f'{day} dia(s) tem {horas_do_dia} horas, {minutos_do_dia} minutos e {segundos_do_dia} segundos.')

