
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])

if food == "grape" or food == "apple":
    print("fruit")
if food == "bacon" or food == "steak":
    print("meat")
if food == "dirt" or food == "worm":
    print("yuck")