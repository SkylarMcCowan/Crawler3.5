class Race:
    def __init__(self, name, traits, languages):
        self.name = name
        self.traits = traits
        self.languages = languages

# Existing races
human = Race(
    name="Human",
    traits=["Bonus feat at 1st level", "Extra skill points"],
    languages=["Common"]
)

elf = Race(
    name="Elf",
    traits=["Immune to sleep", "+2 Dexterity, -2 Constitution"],
    languages=["Common", "Elvish"]
)

# Add new races below

dwarf = Race(
    name="Dwarf",
    traits=["+2 Constitution, -2 Charisma", "Darkvision", "Stonecunning"],
    languages=["Common", "Dwarvish"]
)

halfling = Race(
    name="Halfling",
    traits=["+2 Dexterity, -2 Strength", "Lucky", "Halfling Nimbleness"],
    languages=["Common", "Halfling"]
)

gnome = Race(
    name="Gnome",
    traits=["+2 Constitution, -2 Strength", "Low-Light Vision", "Gnome Cunning"],
    languages=["Common", "Gnomish"]
)

half_elf = Race(
    name="Half-Elf",
    traits=["+2 to Charisma", "Darkvision", "Skill Versatility"],
    languages=["Common", "Elvish"]
)

half_orc = Race(
    name="Half-Orc",
    traits=["+2 Strength, -2 Intelligence", "Darkvision", "Relentless Endurance"],
    languages=["Common", "Orcish"]
)

# Updated core_races list
core_races = [human, elf, dwarf, halfling, gnome, half_elf, half_orc]