#Task 1
place = input("Choose a place: forest or cave? ")
action = 0
light = 0

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    

#Task 2
    light = input("Would you like to light a torch or proceed in the dark? ")
    
    if light == "light a torch":
        print("You make it to the treasure!")
    elif light == "proceed in the dark":
        print("You hit your head and go unconcious")

#Task 3
if place != "forest" or "cave":
    pass
if action != "climb a tree" or "cross a river":
    pass
if light != "light a torch" or "proceed in the dark":
    pass