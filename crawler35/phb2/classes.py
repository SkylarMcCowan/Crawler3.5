class Class:
    def __init__(self, name, hit_die, primary_stat, class_skills, class_abilities, saving_throws=None, armor_proficiencies=None, weapon_proficiencies=None, tool_proficiencies=None, starter_kit=None):
        self.name = name
        self.hit_die = hit_die
        self.primary_stat = primary_stat
        self.class_skills = class_skills
        self.class_abilities = class_abilities
        self.saving_throws = saving_throws
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.starter_kit = starter_kit  # Added starter kit for consistency

# Example supplemental classes with starter kits and saving throws added

beguiler = Class(
    name="Beguiler",
    hit_die="d6",
    primary_stat="Intelligence",
    class_skills=["Bluff", "Hide", "Move Silently", "Spellcraft"],
    class_abilities=["Spellcasting", "Trapfinding"],
    saving_throws=["Reflex", "Will"],  # Strong: Reflex, Will
    starter_kit={
        'weapon': ["Dagger"],
        'armor': ["Leather Armor"],
        'tools': None,
        'items': ["Adventurer's Pack"]
    }
)

duskblade = Class(
    name="Duskblade",
    hit_die="d8",
    primary_stat="Intelligence",
    class_skills=["Concentration", "Jump", "Spellcraft"],
    class_abilities=["Arcane Channeling", "Spellcasting"],
    saving_throws=["Fortitude"],  # Strong: Fortitude; Weak: Reflex, Will
    starter_kit={
        'weapon': ["Longsword"],
        'armor': ["Chainmail"],
        'tools': None,
        'items': ["Adventurer's Pack"]
    }
)

# Psionic Classes
psion = Class(
    name="Psion",
    hit_die="d4",
    primary_stat="Intelligence",
    class_skills=["Concentration", "Autohypnosis", "Knowledge (Psionics)", "Spellcraft"],
    class_abilities=["Psionics", "Discipline Focus", "Psionic Powers"],
    saving_throws=["Will"],  # Strong: Will; Weak: Fortitude, Reflex
    starter_kit={
        'weapon': ["Quarterstaff"],
        'armor': None,
        'tools': ["Psionic Focus"],
        'items': ["Psion's Pack"]
    }
)

soulknife = Class(
    name="Soulknife",
    hit_die="d10",
    primary_stat="Dexterity",
    class_skills=["Tumble", "Climb", "Jump", "Hide", "Move Silently"],
    class_abilities=["Mind Blade", "Psionic Strike", "Throw Mind Blade"],
    saving_throws=["Fortitude", "Reflex"],  # Strong: Fortitude, Reflex
    starter_kit={
        'weapon': ["Mind Blade"],
        'armor': ["Studded Leather"],
        'tools': None,
        'items': ["Adventurer's Pack"]
    }
)

# Additional PHB2 Classes
dragon_shaman = Class(
    name="Dragon Shaman",
    hit_die="d10",
    primary_stat="Charisma",
    class_skills=["Diplomacy", "Intimidate", "Knowledge (Arcana)", "Sense Motive"],
    class_abilities=["Draconic Aura", "Breath Weapon"],
    saving_throws=["Fortitude"],  # Strong: Fortitude; Weak: Reflex, Will
    starter_kit={
        'weapon': ["Warhammer"],
        'armor': ["Scale Mail"],
        'tools': None,
        'items': ["Adventurer's Pack"]
    }
)

knight = Class(
    name="Knight",
    hit_die="d12",
    primary_stat="Charisma",
    class_skills=["Diplomacy", "Handle Animal", "Ride", "Sense Motive"],
    class_abilities=["Knight's Challenge", "Bulwark of Defense"],
    saving_throws=["Fortitude", "Will"],  # Strong: Fortitude, Will; Weak: Reflex
    starter_kit={
        'weapon': ["Lance"],
        'armor': ["Full Plate"],
        'tools': None,
        'items': ["Adventurer's Pack"]
    }
)

spellthief = Class(
    name="Spellthief",
    hit_die="d6",
    primary_stat="Dexterity",
    class_skills=["Bluff", "Hide", "Move Silently", "Spellcraft"],
    class_abilities=["Steal Spell", "Sneak Attack"],
    saving_throws=["Reflex"],  # Strong: Reflex; Weak: Fortitude, Will
    starter_kit={
        'weapon': ["Dagger"],
        'armor': ["Leather Armor"],
        'tools': ["Thieves' Tools"],
        'items': ["Adventurer's Pack"]
    }
)

warmage = Class(
    name="Warmage",
    hit_die="d6",
    primary_stat="Charisma",
    class_skills=["Concentration", "Intimidate", "Knowledge (Arcana)", "Spellcraft"],
    class_abilities=["Spellcasting", "Warmage Edge"],
    saving_throws=["Will"],  # Strong: Will; Weak: Fortitude, Reflex
    starter_kit={
        'weapon': ["Staff"],
        'armor': ["Light Armor"],
        'tools': None,
        'items': ["Adventurer's Pack"]
    }
)

# Combine all classes into a single list
phb2_classes = [beguiler, duskblade, psion, soulknife, dragon_shaman, knight, spellthief, warmage]

# Ensure phb2_classes is exported
__all__ = ['phb2_classes']