import sys
import os
import random
import time
import json

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crawler35.phb1.classes import core_classes, Class
from crawler35.phb1.races import *  # Import PHB1 races
from crawler35.phb2.races import phb2_races  # Import PHB2 races
from crawler35.phb1.items import core_items
from crawler35.phb1.monsters import core_monsters
from crawler35.phb1.spells import core_spells

def display_intro():
    print("===================================")
    print("      Welcome to D&D Crawler 3.5   ")
    print("===================================")
    print("In this game, you will create a character,")
    print("explore dungeons, fight monsters, and find treasure.")
    print("===================================")

def calculate_cost(score):
    """Returns the cost of increasing a score to the next value based on point buy system."""
    if score <= 13:
        return 1
    elif score == 14:
        return 2
    elif score == 15:
        return 2
    elif score == 16:
        return 3
    else:
        return 0  # Max score is 18

def allocate_ability_points():
    abilities = {"Strength": 8, "Dexterity": 8, "Constitution": 8, "Intelligence": 8, "Wisdom": 8, "Charisma": 8}
    points = 27  # Point pool
    
    # Mapping of abbreviations to full ability names
    ability_abbr = {
        "str": "Strength",
        "dex": "Dexterity",
        "con": "Constitution",
        "int": "Intelligence",
        "wis": "Wisdom",
        "cha": "Charisma"
    }
    
    print("\nYou have 27 points to allocate to your abilities.")
    print("Each ability starts at 8. You can spend points to increase the score.")
    print("Max score is 18. Costs: 9-14 (1 point each), 15-16 (2 points each), 17-18 (3 points each).")
    print("Use abbreviations: STR, DEX, CON, INT, WIS, CHA.")
    
    while points > 0:
        print(f"\nRemaining points: {points}")
        for ability, score in abilities.items():
            print(f"{ability}: {score}")
        
        choice = input("\nEnter the ability you want to increase: ").lower()
        if choice in ability_abbr:
            choice = ability_abbr[choice]
        
        if choice in abilities:
            current_score = abilities[choice]
            if current_score >= 18:
                print(f"{choice} is already at the maximum score (18).")
                continue

            cost = calculate_cost(current_score)
            if cost <= points:
                abilities[choice] += 1
                points -= cost
                print(f"\nIncreased {choice} to {abilities[choice]} (Cost: {cost} points)")
            else:
                print("\nNot enough points.")
        else:
            print("\nInvalid ability.")
    
    print("\nFinal ability scores:")
    for ability, score in abilities.items():
        print(f"{ability}: {score}")
    
    return abilities

def display_character_stats(character):
    """Displays the current character's stats during combat, including equipment and potions."""
    print("\n===== Character Stats =====")
    print(f"Name: {character['name']}")
    print(f"HP: {character.get('hp', 'Unknown')}")
    print(f"AC: {character.get('armor_class', 'Unknown')}")
    print(f"EXP: {character['exp']}")
    print(f"Level: {character['level']}")
    print(f"Abilities: {', '.join(character['abilities'].keys())}")
    print("\n===== Equipment =====")
    print(f"Weapon: {character['equipment'].get('weapon', 'None')}")
    print(f"Armor: {character['equipment'].get('armor', 'None')}")
    print(f"Potions: {character['equipment'].get('potions', 0)}")
    print("===========================")

def display_combat_stats(character, monster):
    """Displays the player and enemy stats during combat."""
    print("\n================= Combat Stats =================")
    print(f"{'Player':<20} {'VS':<5} {'Enemy':<20}")
    print(f"{character['name']:<20} {'':<5} {monster.name:<20}")
    print(f"{'HP: ' + str(character.get('hp', 'Unknown')):<20} {'':<5} {'HP: ' + str(monster.hit_points):<20}")
    print(f"{'AC: ' + str(character.get('armor_class', 'Unknown')):<20} {'':<5} {'AC: ' + str(monster.armor_class):<20}")
    print(f"{'Level: ' + str(character['level']):<20} {'':<5} {'Type: ' + monster.name:<20}")
    print("================================================")

def combat(monster, character):
    """Combat function with player and enemy stats displayed."""
    print(f"\nCombat started with {monster.name}!")
    print(f"{monster.name} has {monster.hit_points} HP and AC {monster.armor_class}.")

    while monster.hit_points > 0:
        # Display combat stats before each turn
        display_combat_stats(character, monster)

        # Player's turn
        print("\nYour turn:")
        print("1. Attack")
        print("2. Use Potion")
        print("3. Use Item")
        print("4. Flee")
        choice = input("Choose an action: ")
        
        if choice == "1":
            damage = random.randint(1, 10)  # Random damage for simplicity
            monster.hit_points -= damage
            print(f"You hit the {monster.name} for {damage} damage!")
        elif choice == "2":
            if character['equipment']['potions'] > 0:
                print("You used a potion!")
                character['hp'] = min(character['hp'] + 10, 20)  # Heal 10 HP, max 20
                character['equipment']['potions'] -= 1
            else:
                print("You have no potions left!")
        elif choice == "3":
            print("You used an item!")
            # Implement item logic here
        elif choice == "4":
            print("You fled back to town!")
            return  # Exit combat
        
        # Check if monster is defeated
        if monster.hit_points <= 0:
            print(f"You defeated the {monster.name}!")
            character['exp'] += monster.exp_value  # Award experience points
            check_level_up(character)  # Check if the character levels up
            break

        # Monster's turn
        print(f"\n{monster.name}'s turn:")
        monster_damage = random.randint(1, 12)
        print(f"The {monster.name} attacks you for {monster_damage} damage!")
        character['hp'] -= monster_damage  # Apply monster's damage

        # Check if player is defeated
        if character['hp'] <= 0:
            print(f"\nYou were defeated by the {monster.name}!")
            return  # End combat if player dies

        # Add a delay between turns
        time.sleep(1)

    print("\nCombat ended.")

def select_race():
    races = [human, elf, dwarf] + phb2_races  # Add more races as needed
    print("Select a race:")
    for i, race in enumerate(races):
        print(f"{i + 1}. {race.name}")
    choice = int(input("Enter the number of your choice: ")) - 1
    return races[choice]

def suggest_classes(race):
    race_class_suggestions = {
        "Human": ["Fighter", "Wizard"],
        "Elf": ["Ranger", "Wizard"],
        "Dwarf": ["Cleric", "Fighter"],
        "Halfling": ["Rogue", "Bard"]
    }
    
    suggestions = race_class_suggestions.get(race.name, [])
    print(f"\nSuggested classes for {race.name}: {', '.join(suggestions)}")

def select_class():
    print("\nSelect your class:")
    for index, cls in enumerate(core_classes, start=1):
        print(f"{index}. {cls.name}")
    
    choice = input("\nEnter the number of your class: ")
    try:
        selected_class = core_classes[int(choice) - 1]
        print(f"\nYou selected: {selected_class.name}")
        return selected_class
    except (ValueError, IndexError):
        print("\nInvalid choice. Please try again.")
        return select_class()

def name_hero():
    name = input("\nEnter the name of your hero: ")
    print(f"\nYour hero's name is: {name}")
    return name

def select_adventure():
    adventures = ["The Goblin Cave", "The Haunted Forest", "The Dragon's Lair", "The Sunless Citadel"]
    print("\nSelect your adventure:")
    for index, adventure in enumerate(adventures, start=1):
        print(f"{index}. {adventure}")
    
    choice = input("\nEnter the number of your adventure: ")
    try:
        selected_adventure = adventures[int(choice) - 1]
        print(f"\nYou selected: {selected_adventure}")
        return selected_adventure
    except (ValueError, IndexError):
        print("\nInvalid choice. Please try again.")
        return select_adventure()

def display_character_summary(character):
    print("\n===================================")
    print("         Character Summary         ")
    print("===================================")
    print(f"Name: {character['name']}")
    print(f"Race: {character['race'].name}")
    print(f"Class: {character['class'].name}")
    print(f"Level: {character['level']}")
    print(f"EXP: {character['exp']}")
    print(f"Gold: {character['gold']} GP")
    print("Starter Kit:")
    for item_type, items in character['starter_kit'].items():
        if items:
            print(f"  {item_type.capitalize()}: {', '.join(items) if isinstance(items, list) else items}")
    print("Abilities:")
    for ability, score in character['abilities'].items():
        print(f"  {ability}: {score}")
    print("===================================")

def check_level_up(character):
    level_up_exp = {1: 0, 2: 300, 3: 900, 4: 2700, 5: 6500, 6: 14000, 7: 23000, 8: 34000, 9: 48000, 10: 64000}
    current_level = character['level']
    next_level_exp = level_up_exp.get(current_level + 1, float('inf'))
    
    if character['exp'] >= next_level_exp:
        character['level'] += 1
        print(f"\nCongratulations! {character['name']} has reached level {character['level']}!")

# Commented out saving functionality
# def save_character(character, filename="character.json"):
#     character['race'] = {
#         'name': character['race'].name,
#         'traits': character['race'].traits,
#         'languages': character['race'].languages
#     }
#     character['class'] = {
#         'name': character['class'].name,
#         'hit_die': character['class'].hit_die,
#         'primary_stat': getattr(character['class'], 'primary_stat', None),
#         'saving_throws': getattr(character['class'], 'saving_throws', None),
#         'armor_proficiencies': getattr(character['class'], 'armor_proficiencies', None),
#         'weapon_proficiencies': getattr(character['class'], 'weapon_proficiencies', None),
#         'tool_proficiencies': getattr(character['class'], 'tool_proficiencies', None),
#         'skills': getattr(character['class'], 'skills', None)
#     }
#     with open(filename, 'w') as f:
#         json.dump(character, f)
#     print("\nCharacter saved successfully.")

# def load_character(filename="character.json"):
#     if os.path.exists(filename):
#         try:
#             with open(filename, 'r') as f:
#                 character = json.load(f)
#             # Convert dictionaries back to Race and Class objects
#             character['race'] = Race(
#                 name=character['race']['name'],
#                 traits=character['race']['traits'],
#                 languages=character['race']['languages']
#             )
#             character['class'] = Class(
#                 name=character['class']['name'],
#                 hit_die=character['class']['hit_die'],
#                 primary_stat=character['class'].get('primary_stat', None),
#                 class_skills=character['class'].get('class_skills', None),
#                 class_abilities=character['class'].get('class_abilities', None),
#                 ability_modifiers=character['class'].get('ability_modifiers', None),
#                 saving_throws=character['class'].get('saving_throws', None),
#                 armor_proficiencies=character['class'].get('armor_proficiencies', None),
#                 weapon_proficiencies=character['class'].get('weapon_proficiencies', None),
#                 tool_proficiencies=character['class'].get('tool_proficiencies', None),
#                 skills=character['class'].get('skills', None)
#             )
#             # Ensure HP and armor_class are loaded
#             character['hp'] = character.get('hp', 10)  # Default HP to 10 if missing
#             character['armor_class'] = character.get('armor_class', 10)  # Default AC to 10 if missing
#             print("\nCharacter loaded successfully.")
#             return character
#         except json.JSONDecodeError:
#             print("\nError loading character. Starting a new game.")
#             return None
#     else:
#         print("\nNo saved character found.")
#         return None

def create_character():
    selected_race = select_race()
    selected_class = select_class()
    abilities = allocate_ability_points()

    # Provide a default starter kit if not set in the class
    starter_kit = selected_class.starter_kit or {
        'weapon': ["Simple Weapon"], 
        'armor': ["Light Armor"], 
        'tools': None, 
        'items': ["Adventurer's Pack"]
    }
    
    character = {
        'name': name_hero(),
        'race': selected_race,
        'class': selected_class,
        'level': 1,
        'exp': 0,
        'abilities': abilities,
        'traits': selected_race.traits,
        'gold': selected_class.roll_starting_gold(),
        'starter_kit': starter_kit,  # Use the starter kit from class or default
        'hp': 20,  # Default HP, modify based on class and level
        'armor_class': 10,  # Default AC, modify based on class and equipment
        'equipment': {
            'weapon': "Longsword",  # Example starting weapon
            'armor': "Chainmail",  # Example starting armor
            'potions': 3  # Example starting potions
        }
    }

    display_character_summary(character)
    return character

def run_adventure(adventure, character):
    if adventure == "The Goblin Cave":
        print("\nYou enter the dark and damp Goblin Cave.")
        goblin = core_monsters[0]
        combat(goblin, character)
        print("You find some gold and a mysterious artifact.")
        character['exp'] += 100
    elif adventure == "The Haunted Forest":
        print("\nYou step into the eerie Haunted Forest.")
        ghost = core_monsters[1]
        combat(ghost, character)
        print("You find an ancient scroll and some rare herbs.")
        character['exp'] += 150
    elif adventure == "The Dragon's Lair":
        print("\nYou bravely enter the Dragon's Lair.")
        dragon = core_monsters[2]
        combat(dragon, character)
        print("You find a hoard of treasure and a powerful weapon.")
        character['exp'] += 300
    elif adventure == "The Sunless Citadel":
        print("\nYou descend into the Sunless Citadel.")
        kobold = core_monsters[3]
        combat(kobold, character)
        print("You find a hidden stash of potions and a magical ring.")
        character['exp'] += 200
    else:
        print("\nUnknown adventure. Please select a valid adventure.")

def main():
    display_intro()
    
    # Load or create character
    # character = load_character()  # Disabled loading for now
    character = create_character()  # Always create a new character during testing
    
    # Select an adventure
    selected_adventure = select_adventure()
    print(f"\nYour adventure '{selected_adventure}' will scale to your character level.")
    
    # Run the selected adventure
    run_adventure(selected_adventure, character)
    
    # Save character after adventure (disabled for testing)
    # save_character(character)

if __name__ == "__main__":
    main()