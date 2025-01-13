import random
import time

class Monster:
    def __init__(self, name, hit_points, armor_class, attacks, abilities, exp_value):
        self.name = name
        self.hit_points = hit_points
        self.max_hit_points = hit_points  # Store the maximum hit points
        self.armor_class = armor_class
        self.attacks = attacks
        self.abilities = abilities
        self.exp_value = exp_value

# Define specific monsters for the Goblin Cave adventure
goblin = Monster(
    name="Goblin",
    hit_points=10,
    armor_class=15,
    attacks=[{"name": "Scimitar", "damage": "1d6+2 slashing"}],
    abilities=["Nimble Escape (can Disengage or Hide as a bonus action)"],
    exp_value=50
)

goblin_boss = Monster(
    name="Goblin Boss",
    hit_points=30,
    armor_class=17,
    attacks=[{"name": "Multiattack", "damage": "2x 1d6+2 slashing"}],
    abilities=["Leadership (can grant allies within 30 ft. a +1 bonus to attack rolls and saving throws)"],
    exp_value=150
)

def generate_goblin_boss_name(character):
    if "Orcish" in character.get('languages', []):
        return "Gorak the Mighty"
    else:
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6)).capitalize()

def goblin_cave_adventure(character, combat, rest):
    print("\nYou begin your journey to the Goblin Cave.")
    time.sleep(3)
    print("The road is long and winding, with dense forests on either side.")
    time.sleep(3)
    
    # Chance of encounter on the road
    encounter_chance = random.random()
    if encounter_chance < 0.3:  # 30% chance of encounter
        print("Suddenly, you hear rustling in the bushes...")
        time.sleep(3)
        print("A wild creature jumps out and attacks you!")
        wild_creature = Monster(
            name="Wild Creature",
            hit_points=20,
            armor_class=12,
            attacks=[{"name": "Bite", "damage": "1d8+2 piercing"}],
            abilities=["Keen Senses (advantage on Perception checks)"],
            exp_value=75
        )
        combat(wild_creature, character)
        if character['hp'] <= 0:
            print("You have been defeated by the wild creature.")
            return
        print("You manage to defeat the creature and continue your journey.")
    elif encounter_chance < 0.5:  # 20% chance of meeting a wandering merchant
        print("You encounter a wandering merchant on the road.")
        time.sleep(3)
        print("The merchant greets you warmly and offers to trade goods.")
        if character['race'].name == "Elf":
            print("The merchant recognizes you as an elf and offers you a gift.")
            extra_gold = random.randint(1, 50)
            extra_potions = random.randint(1, 3)
            character['gold'] += extra_gold
            character['equipment']['potions'] += extra_potions  # Correctly update the number of potions
            print(f"The merchant gives you {extra_gold} gold and {extra_potions} potions.")
        else:
            print("You have a pleasant conversation with the merchant and continue your journey.")
    else:
        print("The journey is uneventful, and you make good progress.")
    
    time.sleep(3)
    print("As the sun sets, you decide to set up camp for the night.")
    
    # Night of camping
    while True:
        print("\n===== Camp Menu =====")
        print("1. Rest")
        print("2. Set Traps/Alarms")
        print("3. Sleep in Shifts (requires companion)")
        choice = input("Choose an option: ")

        if choice == "1":
            rest(character, 'safe')
            break
        elif choice == "2":
            rest(character, 'traps')
            break
        elif choice == "3":
            rest(character, 'shifts')
            break
        else:
            print("Invalid choice. Please try again.")
    
    print("You wake up the next morning, feeling refreshed, and continue your journey to the Goblin Cave.")
    time.sleep(3)
    print("\nYou enter the dark and damp Goblin Cave.")
    
    if character['race'].name == "Orc":
        print("The goblins see you and cower in fear. They won't attack you.")
        print("You make your way through the cave unchallenged.")
    else:
        print("You encounter two goblins guarding the entrance!")
        for _ in range(2):
            goblin.hit_points = goblin.max_hit_points  # Reset goblin's health
            combat(goblin, character)
            if character['hp'] <= 0:
                print("You have been defeated by the goblins.")
                return
            time.sleep(3)  # Add sleep to slow down the storyline

    print("You reach the inner chamber of the cave.")
    time.sleep(3)  # Add sleep to slow down the storyline
    boss_name = generate_goblin_boss_name(character)
    if "Orcish" in character.get('languages', []):
        print(f"A fearsome Orc boss named {boss_name} appears and commands the goblins to attack you!")
    else:
        print(f"A fearsome Orc boss named {boss_name} (in gibberish) appears and commands the goblins to attack you!")
    time.sleep(3)  # Add sleep to slow down the storyline

    if character['race'].name != "Orc":
        goblin_boss.hit_points = goblin_boss.max_hit_points  # Reset goblin boss's health
        goblin_boss.name = boss_name  # Set the boss name to the generated name
        combat(goblin_boss, character)
        if character['hp'] <= 0:
            print(f"You have been defeated by {boss_name}.")
            return
        time.sleep(3)  # Add sleep to slow down the storyline

    print(f"You have defeated {boss_name} and cleared the Goblin Cave!")
    time.sleep(3)  # Add sleep to slow down the storyline
    print("You find some gold and a mysterious artifact.")
    character['exp'] += 100
    character['gold'] += random.randint(50, 100)
    character['items'].append("Mysterious Artifact")
    time.sleep(3)  # Add sleep to slow down the storyline