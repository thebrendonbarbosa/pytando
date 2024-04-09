"""
007. Ask the user for their name and their age. Add 1 to their age
and display the output 

[Name] next birthday you will be [new age].

"""

name = input('Enter your name: ')
age = input('Enter your age: ')
age_int = int(age)

new_age = age_int + 1 

print(f'{name} next birthday you will be {new_age}')