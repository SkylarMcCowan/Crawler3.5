import random
import time
import simpleaudio as sa
import sys
import os

# Ensure the parent directory is in the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def display_combat_stats(character, monster):
    """Displays the player and enemy stats during combat."""
    print("\n================= Combat Stats =================")
    print(f"{'Player':<20} {'VS':<5} {'Enemy':<20}")
    print(f"{character['name']:<20} {'':<5} {monster.name:<20}")
    print(f"{'HP: ' + str(character.get('hp', 'Unknown')):<20} {'':<5} {'HP: ' + str(monster.hit_points):<20}")
    print(f"{'AC: ' + str(character.get('armor_class', 'Unknown')):<20} {'':<5} {'AC: ' + str(monster.armor_class):<20}")
    print(f"{'Level: ' + str(character['level']):<20} {'':<5} {'Type: ' + monster.name:<20}")
    print("================================================")

def roll_d20():
    """Rolls a d20 and returns the result."""
    return random.randint(1, 20)

def roll_damage(damage_str):
    """Rolls damage based on a damage string like '1d6+2'."""
    num, die, bonus = damage_str.split('d')[0], damage_str.split('d')[1].split('+')[0], damage_str.split('+')[1]
    return sum(random.randint(1, int(die)) for _ in range(int(num))) + int(bonus)

def get_primary_attribute(character_class):
    """Returns the primary attribute for the given character class."""
    primary_attributes = {
        'Fighter': 'Strength',
        'Wizard': 'Intelligence',
        'Rogue': 'Dexterity',
        'Cleric': 'Wisdom',
        # Add other classes as needed
    }
    return primary_attributes.get(character_class, 'Strength')  # Default to Strength if class not found

def combat(monster, character):
    """Combat function with player and enemy stats displayed."""
    print(f"\nCombat started with {monster.name}!")
    print(f"{monster.name} has {monster.hit_points} HP and AC {monster.armor_class}.")

    # Reset monster's health at the beginning of combat
    monster.hit_points = monster.max_hit_points

    while monster.hit_points > 0 and character['hp'] > 0:
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
            attack_roll = roll_d20() + character['abilities'][get_primary_attribute(character['class'].name)]
            if attack_roll >= monster.armor_class:
                damage = random.randint(1, 10)  # Random damage for simplicity
                monster.hit_points -= damage
                print(f"You hit the {monster.name} for {damage} damage!")
            else:
                print(f"You missed the {monster.name}!")
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
        for attack in monster.attacks:
            attack_roll = roll_d20() + monster.primary_attribute
            if attack_roll >= character['armor_class']:
                damage = roll_damage(attack['damage'])
                print(f"The {monster.name} uses {attack['name']} and deals {damage} damage!")
                character['hp'] -= damage  # Apply monster's damage
            else:
                print(f"The {monster.name} missed you!")

            # Check if player is defeated
            if character['hp'] <= 0:
                print(f"\nYou were defeated by the {monster.name}!")
                wave_obj = sa.WaveObject.from_wave_file('path/to/defeat_sound.wav')  # Load defeat sound
                play_obj = wave_obj.play()  # Play defeat sound
                play_obj.wait_done()  # Wait for sound to finish playing
                time.sleep(100)  # Wait for 5 seconds
                from crawler35.game import main_menu  # Import the main_menu function here
                main_menu(character)  # Return to the main menu if the player dies
                return  # End combat if player dies

        # Add a delay between turns
        time.sleep(1)

    print("\nCombat ended.")