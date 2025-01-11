# filepath: /Users/dev/Documents/Not Work, but work/Dungeon Crawler/Crawler3.5/crawler35/adventures/sunless_citadel.py
from crawler35.phb1.monsters import core_monsters

def sunless_citadel_adventure(character, combat):
    print("\nYou descend into the Sunless Citadel.")
    kobold = core_monsters[3]
    combat(kobold, character)
    print("You find a hidden stash of potions and a magical ring.")
    character['exp'] += 200