class Spell:
    def __init__(self, name, level, school, casting_time, range, duration, description):
        self.name = name
        self.level = level
        self.school = school
        self.casting_time = casting_time
        self.range = range
        self.duration = duration
        self.description = description

# Psionic Powers

mind_thrust = Spell(
    name="Mind Thrust",
    level=1,
    school="Psionics",
    casting_time="1 action",
    range="60 feet",
    duration="Instantaneous",
    description="You target a creature's mind with psionic energy, dealing 1d10 psychic damage."
)

energy_ray = Spell(
    name="Energy Ray",
    level=1,
    school="Psionics",
    casting_time="1 action",
    range="30 feet",
    duration="Instantaneous",
    description="You project a ray of energy that deals 1d6 damage of a chosen type: fire, cold, electricity, or sonic."
)

disintegrate_psionic = Spell(
    name="Psionic Disintegrate",
    level=6,
    school="Psionics",
    casting_time="1 action",
    range="60 feet",
    duration="Instantaneous",
    description="A thin ray of psionic energy reduces a creature or object to dust, dealing 10d6+40 force damage."
)

# Add the new psionic powers to the list
phb2_spells = [mind_thrust, energy_ray, disintegrate_psionic]