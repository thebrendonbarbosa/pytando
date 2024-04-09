"""
005. Ask the user to enter three
numbers. Add together the first
two numbers and then multiply
this total by the third. Display the
answer as 
The answer is [answer].

"""


num_1 = input('Enter a number: ')
num_2 = input('Enter other number: ')
num_3 = input('Enter other number: ')

num_1_int = int(num_1)
num_2_int = int(num_2)
num_3_int = int(num_3)

sum = num_1_int + num_2_int
total = sum * num_3_int

print(f'The answer is {total}.')