class Monster:
    def __init__(self, name, hit_points, armor_class, attacks, abilities, exp_value):
        self.name = name
        self.hit_points = hit_points
        self.armor_class = armor_class
        self.attacks = attacks
        self.abilities = abilities
        self.exp_value = exp_value  # Add experience value for each monster

# Existing monsters with exp_value added
goblin = Monster(
    name="Goblin",
    hit_points=7,
    armor_class=15,
    attacks=[{"name": "Scimitar", "damage": "1d6 slashing"}],
    abilities=["Darkvision", "Nimble Escape"],
    exp_value=50  # Example: 50 XP for defeating a Goblin
)

dragon = Monster(
    name="Dragon",
    hit_points=100,
    armor_class=19,
    attacks=[{"name": "Bite", "damage": "2d10 piercing"}, {"name": "Fire Breath", "damage": "8d6 fire"}],
    abilities=["Flying", "Fire Immunity"],
    exp_value=1000  # Example: 1000 XP for defeating a Dragon
)

orc = Monster(
    name="Orc",
    hit_points=15,
    armor_class=13,
    attacks=[{"name": "Greataxe", "damage": "1d12 slashing"}],
    abilities=["Aggressive", "Darkvision"],
    exp_value=100  # Example: 100 XP for defeating an Orc
)

kobold = Monster(
    name="Kobold",
    hit_points=5,
    armor_class=12,
    attacks=[{"name": "Dagger", "damage": "1d4 piercing"}],
    abilities=["Pack Tactics", "Sunlight Sensitivity"],
    exp_value=25  # Example: 25 XP for defeating a Kobold
)

ogre = Monster(
    name="Ogre",
    hit_points=34,
    armor_class=11,
    attacks=[{"name": "Greatclub", "damage": "2d8+4 bludgeoning"}],
    abilities=["Brute"],
    exp_value=200  # Example: 200 XP for defeating an Ogre
)

troll = Monster(
    name="Troll",
    hit_points=63,
    armor_class=16,
    attacks=[{"name": "Claw", "damage": "1d6+5 slashing"}, {"name": "Bite", "damage": "1d6+5 piercing"}],
    abilities=["Regeneration", "Darkvision"],
    exp_value=350  # Example: 350 XP for defeating a Troll
)

# Updated core_monsters list
core_monsters = [goblin, dragon, orc, kobold, ogre, troll]