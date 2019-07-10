
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])

if food == "grape" or food == "apple":
    print("The random choice is "+ food +" and this is fruit.")
if food == "bacon" or food == "steak":
    print("The random choice is "+ food +" and this is meat.")
if food == "dirt" or food == "worm":
    print("The random choice is "+ food +" and this is yuck.")