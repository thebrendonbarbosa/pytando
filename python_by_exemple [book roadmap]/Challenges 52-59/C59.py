"""Display five colours and ask the user to pick one. If they 
pick the same as the program has chosen, say “Well 
done”, otherwise display a witty answer which involves 
the correct colour, e.g. “I bet you are GREEN with envy” 
or “You are probably feeling BLUE right now”. Ask 
them to guess again; if they have still not got it right, 
keep giving them the same clue and ask the user to 
enter a colour until they guess it correctly."""

import random as rd

color = ['Black', 'Purple', 'Green','Yellow','Gray']
print('Choose one color between Black, Purple, Green, Yellow and Gray.')

color_chosen_by_programa = rd.choice(color)

color_user = input('Pick one color: ')

while color_user != color_chosen_by_programa:
    print(f'You are probably feeling {color_chosen_by_programa} right now!')
    color_user = input('Pick one color again: ')

print('Well done')