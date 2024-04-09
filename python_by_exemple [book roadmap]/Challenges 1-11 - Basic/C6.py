"""
006. Ask how many slices of pizza the user
started with and ask how many slices
they have eaten.
Work out how many slices they have left
and display the answer in a user-friendly format.
"""

slices_started = input('How many slides of pizza do you started with? ')
slices_eaten = input('How many slices have you eaten? ')


slices_started_int = int(slices_started)
slices_eaten_int = int(slices_eaten)


slice_left = slices_started_int - slices_eaten_int

print(f'You started with {slices_started_int} slices of pizza, ate {slices_eaten_int} and still missing {slice_left} slices of pizza.')