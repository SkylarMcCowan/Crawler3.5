import random

class Class:
    def __init__(self, name, hit_die, primary_stat, class_skills, class_abilities, ability_modifiers, saving_throws=None, armor_proficiencies=None, weapon_proficiencies=None, tool_proficiencies=None, starter_kit=None, gold_roll=None, skills=None):
        self.name = name
        self.hit_die = hit_die
        self.primary_stat = primary_stat
        self.class_skills = class_skills
        self.class_abilities = class_abilities
        self.ability_modifiers = ability_modifiers
        self.saving_throws = saving_throws
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.starter_kit = starter_kit
        self.gold_roll = gold_roll
        self.skills = skills  # Added skills parameter

    def roll_starting_gold(self):
        """Rolls for starting gold based on the gold_roll formula."""
        if self.gold_roll:
            return sum(random.randint(1, die) for die in self.gold_roll) * 10
        return 0

# Example classes with starter kits added

fighter = Class(
    name="Fighter",
    hit_die="d10",
    primary_stat="Strength",
    class_skills=["Climb", "Jump", "Swim", "Ride"],
    class_abilities=["Bonus Feats", "Weapon Specialization"],
    ability_modifiers={"Strength": +2},
    saving_throws=["Fortitude"],  # Strong: Fortitude; Weak: Reflex, Will
    skills=["Athletics", "Survival"],
    starter_kit={
        'weapon': ["Longsword"],
        'armor': ["Chainmail"],
        'tools': None,
        'items': ["Adventurer's Pack"]
    }
)

wizard = Class(
    name="Wizard",
    hit_die="d4",
    primary_stat="Intelligence",
    class_skills=["Concentration", "Spellcraft", "Knowledge (Arcana)"],
    class_abilities=["Spellcasting", "Familiar"],
    ability_modifiers={"Intelligence": +2},
    saving_throws=["Will"],  # Strong: Will; Weak: Fortitude, Reflex
    skills=["Arcana", "History"],
    starter_kit={
        'weapon': ["Quarterstaff"],
        'armor': None,
        'tools': ["Spellbook"],
        'items': ["Component Pouch", "Adventurer's Pack"]
    }
)

cleric = Class(
    name="Cleric",
    hit_die="d8",
    primary_stat="Wisdom",
    class_skills=["Concentration", "Heal", "Knowledge (Religion)"],
    class_abilities=["Turn Undead", "Divine Spells"],
    ability_modifiers={"Wisdom": +2},
    saving_throws=["Fortitude", "Will"],  # Strong: Fortitude, Will; Weak: Reflex
    skills=["Religion", "Insight"],
    starter_kit={
        'weapon': ["Mace"],
        'armor': ["Chainmail"],
        'tools': ["Holy Symbol"],
        'items': ["Healer's Kit", "Adventurer's Pack"]
    }
)

rogue = Class(
    name="Rogue",
    hit_die="d6",
    primary_stat="Dexterity",
    class_skills=["Stealth", "Acrobatics", "Sleight of Hand"],
    class_abilities=["Sneak Attack", "Evasion"],
    ability_modifiers={"Dexterity": +2},
    saving_throws=["Reflex"],  # Strong: Reflex; Weak: Fortitude, Will
    skills=["Stealth", "Thievery"],
    starter_kit={
        'weapon': ["Dagger", "Shortsword"],
        'armor': ["Leather Armor"],
        'tools': ["Thieves' Tools"],
        'items': ["Rope", "Adventurer's Pack"]
    }
)

bard = Class(
    name="Bard",
    hit_die="d6",
    primary_stat="Charisma",
    class_skills=["Perform", "Diplomacy", "Bluff"],
    class_abilities=["Bardic Inspiration", "Spellcasting"],
    ability_modifiers={"Charisma": +2},
    saving_throws=["Reflex", "Will"],  # Strong: Reflex, Will; Weak: Fortitude
    skills=["Performance", "Persuasion"],
    starter_kit={
        'weapon': ["Rapier", "Shortbow"],
        'armor': ["Leather Armor"],
        'tools': ["Lute"],
        'items': ["Adventurer's Pack"]
    }
)

ranger = Class(
    name="Ranger",
    hit_die="d10",
    primary_stat="Dexterity",
    class_skills=["Survival", "Perception", "Stealth"],
    class_abilities=["Favored Enemy", "Spellcasting"],
    ability_modifiers={"Dexterity": +2},
    saving_throws=["Fortitude", "Reflex"],  # Strong: Fortitude, Reflex; Weak: Will
    skills=["Nature", "Perception"],
    starter_kit={
        'weapon': ["Longbow"],
        'armor': ["Leather Armor"],
        'tools': None,
        'items': ["Adventurer's Pack"]
    }
)

paladin = Class(
    name="Paladin",
    hit_die="d10",
    primary_stat="Strength",
    class_skills=["Heal", "Diplomacy", "Sense Motive"],
    class_abilities=["Divine Smite", "Lay on Hands"],
    ability_modifiers={"Strength": +2},
    saving_throws=["Fortitude"],  # Strong: Fortitude; Weak: Reflex, Will
    skills=["Religion", "Persuasion"],
    starter_kit={
        'weapon': ["Warhammer"],
        'armor': ["Chainmail"],
        'tools': ["Holy Symbol"],
        'items': ["Adventurer's Pack"]
    }
)

sorcerer = Class(
    name="Sorcerer",
    hit_die="d4",
    primary_stat="Charisma",
    class_skills=["Concentration", "Spellcraft", "Bluff"],
    class_abilities=["Spellcasting", "Sorcerous Origin"],
    ability_modifiers={"Charisma": +2},
    saving_throws=["Will"],  # Strong: Will; Weak: Fortitude, Reflex
    skills=["Arcana", "Deception"],
    starter_kit={
        'weapon': ["Dagger"],
        'armor': None,
        'tools': ["Component Pouch"],
        'items': ["Adventurer's Pack"]
    }
)

druid = Class(
    name="Druid",
    hit_die="d8",
    primary_stat="Wisdom",
    class_skills=["Nature", "Survival", "Animal Handling"],
    class_abilities=["Wild Shape", "Spellcasting"],
    ability_modifiers={"Wisdom": +2},
    saving_throws=["Fortitude", "Will"],  # Strong: Fortitude, Will; Weak: Reflex
    skills=["Animal Handling", "Nature"],
    starter_kit={
        'weapon': ["Club"],
        'armor': ["Leather Armor"],
        'tools': None,
        'items': ["Healer's Kit", "Adventurer's Pack"]
    }
)

monk = Class(
    name="Monk",
    hit_die="d8",
    primary_stat="Dexterity",
    class_skills=["Acrobatics", "Athletics", "Stealth"],
    class_abilities=["Martial Arts", "Ki"],
    ability_modifiers={"Dexterity": +2},
    saving_throws=["Fortitude", "Reflex", "Will"],  # Strong in all saving throws
    skills=["Athletics", "Acrobatics"],
    starter_kit={
        'weapon': ["Quarterstaff"],
        'armor': None,
        'tools': None,
        'items': ["Adventurer's Pack"]
    }
)

barbarian = Class(
    name="Barbarian",
    hit_die="d12",
    primary_stat="Strength",
    class_skills=["Athletics", "Survival", "Intimidation"],
    class_abilities=["Rage", "Unarmored Defense"],
    ability_modifiers={"Strength": +2},
    saving_throws=["Fortitude"],  # Strong: Fortitude; Weak: Reflex, Will
    skills=["Survival", "Intimidation"],
    starter_kit={
        'weapon': ["Greataxe"],
        'armor': ["Hide Armor"],
        'tools': None,
        'items': ["Adventurer's Pack"]
    }
)

# Updated core_classes list with all classes
core_classes = [
    fighter, wizard, cleric, rogue, bard, ranger, paladin, sorcerer, druid, monk, barbarian
]

# Ensure core_classes is exported
__all__ = ['core_classes']