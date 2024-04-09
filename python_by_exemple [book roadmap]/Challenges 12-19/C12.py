"""
012. Ask for two numbers. If
the first one is larger
than the second, display
the second number first
and then the first
number, otherwise show
the first number first and
then the second.
"""


number1 = input('Enter a number: ')
number1_float = float(number1)

number2 = input('Enter other number: ')
number2_float = float(number2)


if number1_float > number2_float and number1_float == number2_float :
    print(number2_float, number1_float)
else:
    print(number1_float, number2_float) 