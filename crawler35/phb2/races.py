class Race:
    def __init__(self, name, traits, languages):
        self.name = name
        self.traits = traits
        self.languages = languages

# Example supplemental races
goliath = Race(
    name="Goliath",
    traits=["Powerful Build", "Mountain Movement", "Stone's Endurance", "+4 Strength, -2 Dexterity"],
    languages=["Common", "Giant"]
)

raptoran = Race(
    name="Raptoran",
    traits=["Flight", "+2 Dexterity"],
    languages=["Common", "Auran"]
)

elan = Race(
    name="Elan",
    traits=["Naturally Psionic", "Resistance to Psionic Powers"],
    languages=["Common", "Telepathy"]
)

duergar = Race(
    name="Duergar",
    traits=["+2 Constitution, -2 Charisma", "Darkvision", "Psionic Invisibility"],
    languages=["Common", "Dwarvish", "Undercommon"]
)

shifter = Race(
    name="Shifter",
    traits=["Shifting", "Low-Light Vision", "Beasthide", "+2 Dexterity, +2 Wisdom, -2 Charisma"],
    languages=["Common"]
)

phb2_races = [goliath, raptoran, elan, duergar, shifter]