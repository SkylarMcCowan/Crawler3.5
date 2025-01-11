class Monster:
    def __init__(self, name, hit_points, armor_class, attacks, abilities, exp_value):
        self.name = name
        self.hit_points = hit_points
        self.armor_class = armor_class
        self.attacks = attacks
        self.abilities = abilities
        self.exp_value = exp_value  # Experience value for defeating the monster

# Basic monsters for early adventures
goblin = Monster(
    name="Goblin",
    hit_points=7,
    armor_class=15,
    attacks=[{"name": "Scimitar", "damage": "1d6 slashing"}],
    abilities=["Darkvision 60 ft.", "Nimble Escape (Disengage or Hide as a bonus action)"],
    exp_value=50
)

skeleton_warrior = Monster(
    name="Skeleton Warrior",
    hit_points=13,
    armor_class=13,
    attacks=[{"name": "Rusty Sword", "damage": "1d6 slashing"}],
    abilities=["Darkvision 60 ft.", "Damage Vulnerabilities: Bludgeoning", "Damage Immunities: Poison"],
    exp_value=50
)

ghoul = Monster(
    name="Ghoul",
    hit_points=22,
    armor_class=14,
    attacks=[{"name": "Claw", "damage": "1d6 slashing"}, {"name": "Bite", "damage": "1d6 piercing"}],
    abilities=["Paralyzing Touch (DC 12 save)", "Darkvision 60 ft.", "Undead Immunities"],
    exp_value=200
)

giant_centipede = Monster(
    name="Giant Centipede",
    hit_points=9,
    armor_class=13,
    attacks=[{"name": "Bite", "damage": "1d4 piercing plus poison"}],
    abilities=["Poison (DC 11 save or take 1d6 poison damage)", "Climber"],
    exp_value=50
)

dire_wolf_pup = Monster(
    name="Dire Wolf Pup",
    hit_points=15,
    armor_class=12,
    attacks=[{"name": "Bite", "damage": "1d8 piercing"}],
    abilities=["Pack Tactics", "Keen Hearing and Smell"],
    exp_value=100
)
animated_broom = Monster(
    name="Animated Broom",
    hit_points=18,
    armor_class=15,
    attacks=[{"name": "Sweep Strike", "damage": "1d6 bludgeoning"}],
    abilities=["Magic Resistance", "False Appearance (appears as a mundane object when not attacking)"],
    exp_value=75
)
giant_fire_beetle = Monster(
    name="Giant Fire Beetle",
    hit_points=8,
    armor_class=13,
    attacks=[{"name": "Bite", "damage": "1d6 piercing"}],
    abilities=["Bioluminescence (provides light in a 10-ft. radius)"],
    exp_value=25
)
bandit_leader = Monster(
    name="Bandit Leader",
    hit_points=30,
    armor_class=14,
    attacks=[{"name": "Shortsword", "damage": "1d6+2 piercing"}, {"name": "Crossbow", "damage": "1d8 piercing"}],
    abilities=["Tactical Awareness (advantage on initiative checks)"],
    exp_value=150
)

mud_elemental = Monster(
    name="Mud Elemental",
    hit_points=20,
    armor_class=12,
    attacks=[{"name": "Mud Slam", "damage": "1d8 bludgeoning"}],
    abilities=["Mud Form (can squeeze through tight spaces)", "Amorphous"],
    exp_value=100
)

kobold = Monster(
    name="Kobold",
    hit_points=5,
    armor_class=12,
    attacks=[{"name": "Dagger", "damage": "1d4 piercing"}],
    abilities=["Darkvision 60 ft.", "Pack Tactics (advantage on attack rolls if an ally is within 5 ft.)", "Sunlight Sensitivity"],
    exp_value=25
)

giant_rat = Monster(
    name="Giant Rat",
    hit_points=7,
    armor_class=12,
    attacks=[{"name": "Bite", "damage": "1d4 piercing"}],
    abilities=["Darkvision 60 ft.", "Pack Tactics"],
    exp_value=25
)

wolf = Monster(
    name="Wolf",
    hit_points=11,
    armor_class=13,
    attacks=[{"name": "Bite", "damage": "2d4+2 piercing"}],
    abilities=["Darkvision 60 ft.", "Pack Tactics", "Keen Hearing and Smell (advantage on Perception checks using hearing or smell)"],
    exp_value=50
)

bandit = Monster(
    name="Bandit",
    hit_points=11,
    armor_class=12,
    attacks=[{"name": "Scimitar", "damage": "1d6+1 slashing"}, {"name": "Light Crossbow", "damage": "1d8 piercing"}],
    abilities=["Darkvision 60 ft.", "Thuggish (advantage on Intimidation checks)"],
    exp_value=25
)

orc = Monster(
    name="Orc",
    hit_points=15,
    armor_class=13,
    attacks=[{"name": "Greataxe", "damage": "1d12+3 slashing"}],
    abilities=["Darkvision 60 ft.", "Aggressive (as a bonus action, move up to its speed toward a hostile creature)"],
    exp_value=100
)

skeleton = Monster(
    name="Skeleton",
    hit_points=13,
    armor_class=13,
    attacks=[{"name": "Shortsword", "damage": "1d6+2 piercing"}, {"name": "Shortbow", "damage": "1d6 piercing"}],
    abilities=["Darkvision 60 ft.", "Damage Vulnerabilities: Bludgeoning", "Damage Immunities: Poison"],
    exp_value=50
)

zombie = Monster(
    name="Zombie",
    hit_points=22,
    armor_class=8,
    attacks=[{"name": "Slam", "damage": "1d6+1 bludgeoning"}],
    abilities=["Darkvision 60 ft.", "Undead Fortitude (DC 5 + damage taken to avoid being reduced to 0 HP)"],
    exp_value=100
)

giant_spider = Monster(
    name="Giant Spider",
    hit_points=26,
    armor_class=14,
    attacks=[{"name": "Bite", "damage": "1d8+3 piercing plus poison"}],
    abilities=["Darkvision 60 ft.", "Spider Climb", "Web Sense", "Web (Recharge 5–6)"],
    exp_value=200
)

# Core monster list for early game adventures
core_monsters = [goblin, kobold, giant_rat, wolf, bandit, orc, skeleton, zombie, 
                 giant_spider, skeleton_warrior, ghoul, giant_centipede, dire_wolf_pup, 
                 animated_broom, giant_fire_beetle, bandit_leader, mud_elemental
                 ]