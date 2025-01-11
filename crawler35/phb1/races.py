# filepath: /Users/dev/Documents/Not Work, but work/Dungeon Crawler/Crawler3.5/crawler35/phb1/races.py
class Race:
    def __init__(self, name, traits, languages, ability_modifiers):
        self.name = name
        self.traits = traits
        self.languages = languages
        self.ability_modifiers = ability_modifiers

# Existing races
human = Race(
    name="Human",
    traits=["Bonus feat at 1st level", "4 extra skill points at 1st level and 1 extra skill point per level"],
    languages=["Common"],
    ability_modifiers={}
)

elf = Race(
    name="Elf",
    traits=["+2 Dexterity, -2 Constitution", "Immune to sleep effects", "+2 saving throw bonus against enchantment spells", "Low-Light Vision", "Keen Senses (+2 on Listen, Search, and Spot checks)"],
    languages=["Common", "Elvish"],
    ability_modifiers={"Dexterity": 2, "Constitution": -2}
)

# Add new races below

dwarf = Race(
    name="Dwarf",
    traits=["+2 Constitution, -2 Charisma", "Darkvision 60 ft.", "+2 on saving throws against poison and spells", "+1 attack bonus against orcs and goblinoids", "+4 dodge bonus to AC against giants", "Stonecunning (+2 on Search checks for stonework)"],
    languages=["Common", "Dwarvish"],
    ability_modifiers={"Constitution": 2, "Charisma": -2}
)

halfling = Race(
    name="Halfling",
    traits=["+2 Dexterity, -2 Strength", "+1 on all saving throws", "+2 morale bonus on saving throws against fear", "+1 attack bonus with thrown weapons and slings", "+2 on Listen checks"],
    languages=["Common", "Halfling"],
    ability_modifiers={"Dexterity": 2, "Strength": -2}
)

gnome = Race(
    name="Gnome",
    traits=["+2 Constitution, -2 Strength", "Low-Light Vision", "+2 saving throw bonus against illusions", "+1 DC for illusion spells cast", "+1 attack bonus against kobolds and goblinoids", "+4 dodge bonus to AC against giants", "+2 on Listen and Craft (alchemy) checks"],
    languages=["Common", "Gnomish"],
    ability_modifiers={"Constitution": 2, "Strength": -2}
)

half_elf = Race(
    name="Half-Elf",
    traits=["+2 Diplomacy and Gather Information", "+1 on Listen, Search, and Spot checks", "Immune to sleep effects", "+2 saving throw bonus against enchantment spells", "Low-Light Vision"],
    languages=["Common", "Elvish"],
    ability_modifiers={}
)

half_orc = Race(
    name="Half-Orc",
    traits=["+2 Strength, -2 Intelligence, -2 Charisma", "Darkvision 60 ft.", "Orc Blood (counts as orc for effects and magic items)"],
    languages=["Common", "Orcish"],
    ability_modifiers={"Strength": 2, "Intelligence": -2, "Charisma": -2}
)

orc = Race(
    name="Orc",
    traits=["+4 Strength, -2 Intelligence, -2 Wisdom, -2 Charisma", "Darkvision 60 ft.", "Light Sensitivity (-1 on attack rolls and Spot checks in bright sunlight or within the radius of a daylight spell)", "Orc Blood (counts as orc for effects and magic items)"],
    languages=["Common", "Orcish"],
    ability_modifiers={"Strength": 4, "Intelligence": -2, "Wisdom": -2, "Charisma": -2}
)

drow = Race(
    name="Drow",
    traits=[
        "+2 Dexterity, -2 Constitution, +2 Charisma",
        "Darkvision 120 ft.",
        "Light Blindness (blinded for 1 round in bright light, -1 on attack rolls, saves, and checks while in bright light)",
        "+2 on Will saves against spells and spell-like abilities",
        "+2 on Listen, Search, and Spot checks",
        "Keen Senses (automatic Search check to detect secret doors within 5 feet)",
        "Spell Resistance (SR 11 + class levels)",
        "Spell-Like Abilities (1/day: dancing lights, darkness, and faerie fire)",
        "Weapon Familiarity (proficient with rapiers, short swords, and hand crossbows)"
    ],
    languages=["Common", "Elvish", "Undercommon"],
    ability_modifiers={"Dexterity": 2, "Constitution": -2, "Charisma": 2}
)

# Updated core_races list
core_races = [human, elf, dwarf, halfling, gnome, half_elf, half_orc, orc, drow]