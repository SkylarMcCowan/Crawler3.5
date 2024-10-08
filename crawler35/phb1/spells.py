class Spell:
    def __init__(self, name, level, school, casting_time, range, duration, description):
        self.name = name
        self.level = level
        self.school = school
        self.casting_time = casting_time
        self.range = range
        self.duration = duration
        self.description = description

# Core spells from PHB1, organized by level

# Level 0 (Cantrips)
ray_of_frost = Spell(
    name="Ray of Frost",
    level=0,
    school="Evocation",
    casting_time="1 action",
    range="60 feet",
    duration="Instantaneous",
    description="A frigid beam of blue-white light streaks toward a creature within range, dealing 1d3 cold damage."
)

light = Spell(
    name="Light",
    level=0,
    school="Evocation",
    casting_time="1 action",
    range="Touch",
    duration="1 hour",
    description="You touch one object and cause it to emit bright light in a 20-foot radius."
)

mage_hand = Spell(
    name="Mage Hand",
    level=0,
    school="Transmutation",
    casting_time="1 action",
    range="30 feet",
    duration="1 minute",
    description="A spectral, floating hand appears at a point you choose, allowing you to manipulate objects."
)

detect_magic = Spell(
    name="Detect Magic",
    level=0,
    school="Divination",
    casting_time="1 action",
    range="Self",
    duration="Concentration, up to 10 minutes",
    description="You sense the presence of magic within 30 feet of you."
)

# Level 1 Spells
magic_missile = Spell(
    name="Magic Missile",
    level=1,
    school="Evocation",
    casting_time="1 action",
    range="120 feet",
    duration="Instantaneous",
    description="Creates three glowing darts of magical force. Each dart hits a target of your choice for 1d4+1 force damage."
)

shield = Spell(
    name="Shield",
    level=1,
    school="Abjuration",
    casting_time="1 reaction",
    range="Self",
    duration="1 round",
    description="An invisible barrier of magical force appears and protects you. You gain +5 AC until the start of your next turn."
)

cure_light_wounds = Spell(
    name="Cure Light Wounds",
    level=1,
    school="Evocation",
    casting_time="1 action",
    range="Touch",
    duration="Instantaneous",
    description="A creature you touch regains 1d8+your spellcasting modifier hit points."
)

burning_hands = Spell(
    name="Burning Hands",
    level=1,
    school="Evocation",
    casting_time="1 action",
    range="Self (15-foot cone)",
    duration="Instantaneous",
    description="A cone of flame shoots from your fingertips, dealing 3d6 fire damage to creatures in the area."
)

identify = Spell(
    name="Identify",
    level=1,
    school="Divination",
    casting_time="1 minute",
    range="Touch",
    duration="Instantaneous",
    description="You learn the properties and how to use one magical item or object you touch."
)

# Level 2 Spells
invisibility = Spell(
    name="Invisibility",
    level=2,
    school="Illusion",
    casting_time="1 action",
    range="Touch",
    duration="Concentration, up to 1 hour",
    description="A creature you touch becomes invisible until the spell ends. The spell ends if the target attacks or casts a spell."
)

spiritual_weapon = Spell(
    name="Spiritual Weapon",
    level=2,
    school="Evocation",
    casting_time="1 bonus action",
    range="60 feet",
    duration="1 minute",
    description="You create a floating, spectral weapon that lasts for the duration or until you cast this spell again. You can use a bonus action to attack with it."
)

mirror_image = Spell(
    name="Mirror Image",
    level=2,
    school="Illusion",
    casting_time="1 action",
    range="Self",
    duration="1 minute",
    description="Three illusory duplicates of yourself appear in your space, confusing attackers."
)

# Level 3 Spells
fireball = Spell(
    name="Fireball",
    level=3,
    school="Evocation",
    casting_time="1 action",
    range="150 feet",
    duration="Instantaneous",
    description="A bright streak flashes from your pointing finger to a point you choose. It explodes in a 20-foot radius, dealing 8d6 fire damage."
)

haste = Spell(
    name="Haste",
    level=3,
    school="Transmutation",
    casting_time="1 action",
    range="30 feet",
    duration="Concentration, up to 1 minute",
    description="Choose a willing creature you can see. Its speed is doubled, it gains a +2 bonus to AC, and it can make an additional action on each of its turns."
)

counterspell = Spell(
    name="Counterspell",
    level=3,
    school="Abjuration",
    casting_time="1 reaction",
    range="60 feet",
    duration="Instantaneous",
    description="You attempt to interrupt a creature in the process of casting a spell. The creature’s spell fails and has no effect."
)

# Level 4 Spells
greater_invisibility = Spell(
    name="Greater Invisibility",
    level=4,
    school="Illusion",
    casting_time="1 action",
    range="Touch",
    duration="Concentration, up to 1 minute",
    description="You or a creature you touch becomes invisible until the spell ends. Any action does not break invisibility."
)

dimension_door = Spell(
    name="Dimension Door",
    level=4,
    school="Conjuration",
    casting_time="1 action",
    range="500 feet",
    duration="Instantaneous",
    description="You teleport yourself and up to one willing creature to a destination within range."
)

# Level 5 Spells
cone_of_cold = Spell(
    name="Cone of Cold",
    level=5,
    school="Evocation",
    casting_time="1 action",
    range="Self (60-foot cone)",
    duration="Instantaneous",
    description="A blast of cold air erupts from your hands, dealing 8d8 cold damage to creatures in a 60-foot cone."
)

teleport = Spell(
    name="Teleport",
    level=5,
    school="Conjuration",
    casting_time="1 action",
    range="Unlimited",
    duration="Instantaneous",
    description="This spell instantly transports you and up to eight willing creatures to a destination you specify."
)

# Core spell list, organized for easy reference
core_spells = [
    # Level 0 Cantrips
    ray_of_frost, light, mage_hand, detect_magic,
    
    # Level 1 Spells
    magic_missile, cure_light_wounds, shield, burning_hands, identify,
    
    # Level 2 Spells
    invisibility, spiritual_weapon, mirror_image,
    
    # Level 3 Spells
    fireball, haste, counterspell,
    
    # Level 4 Spells
    greater_invisibility, dimension_door,
    
    # Level 5 Spells
    cone_of_cold, teleport
]
