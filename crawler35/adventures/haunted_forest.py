# filepath: /Users/dev/Documents/Not Work, but work/Dungeon Crawler/Crawler3.5/crawler35/adventures/haunted_forest.py
from crawler35.phb1.monsters import core_monsters

def haunted_forest_adventure(character, combat):
    print("\nYou step into the eerie Haunted Forest.")
    ghost = core_monsters[1]
    combat(ghost, character)
    print("You find an ancient scroll and some rare herbs.")
    character['exp'] += 150