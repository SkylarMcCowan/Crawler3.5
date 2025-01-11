# filepath: /Users/dev/Documents/Not Work, but work/Dungeon Crawler/Crawler3.5/crawler35/adventures/dragons_lair.py
from crawler35.phb1.monsters import core_monsters

def dragons_lair_adventure(character, combat):
    print("\nYou bravely enter the Dragon's Lair.")
    dragon = core_monsters[2]
    combat(dragon, character)
    print("You find a hoard of treasure and a powerful weapon.")
    character['exp'] += 300