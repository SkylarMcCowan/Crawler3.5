class Item:
    def __init__(self, name, item_type, cost, properties):
        self.name = name
        self.item_type = item_type
        self.cost = cost
        self.properties = properties

# Weapons
handaxe = Item(
    name="Handaxe",
    item_type="Weapon",
    cost="5 gp",
    properties=["1d6 slashing", "Light", "Thrown (range 20/60)"]
)

morningstar = Item(
    name="Morningstar",
    item_type="Weapon",
    cost="15 gp",
    properties=["1d8 piercing"]
)

scimitar = Item(
    name="Scimitar",
    item_type="Weapon",
    cost="25 gp",
    properties=["1d6 slashing", "Finesse", "Light"]
)

warhammer = Item(
    name="Warhammer",
    item_type="Weapon",
    cost="15 gp",
    properties=["1d8 bludgeoning", "Versatile (1d10 when used two-handed)"]
)

rapier = Item(
    name="Rapier",
    item_type="Weapon",
    cost="25 gp",
    properties=["1d8 piercing", "Finesse"]
)

longbow = Item(
    name="Longbow",
    item_type="Weapon",
    cost="50 gp",
    properties=["1d8 piercing", "Ammunition (range 150/600)", "Heavy", "Two-handed"]
)

longsword = Item(
    name="Longsword",
    item_type="Weapon",
    cost="15 gp",
    properties=["1d8 slashing", "Versatile (1d10 when used two-handed)"]
)

dagger = Item(
    name="Dagger",
    item_type="Weapon",
    cost="2 gp",
    properties=["1d4 piercing", "Finesse", "Thrown (range 20 ft)"]
)

greatsword = Item(
    name="Greatsword",
    item_type="Weapon",
    cost="50 gp",
    properties=["2d6 slashing", "Heavy", "Two-handed"]
)

shortbow = Item(
    name="Shortbow",
    item_type="Weapon",
    cost="30 gp",
    properties=["1d6 piercing", "Ammunition (range 80/320)", "Two-handed"]
)

battleaxe = Item(
    name="Battleaxe",
    item_type="Weapon",
    cost="10 gp",
    properties=["1d8 slashing", "Versatile (1d10 when used two-handed)"]
)

# Additional Weapons
mace = Item(
    name="Mace",
    item_type="Weapon",
    cost="5 gp",
    properties=["1d6 bludgeoning"]
)

spear = Item(
    name="Spear",
    item_type="Weapon",
    cost="1 gp",
    properties=["1d6 piercing", "Thrown (range 20 ft)", "Versatile (1d8 when used two-handed)"]
)

crossbow = Item(
    name="Crossbow",
    item_type="Weapon",
    cost="25 gp",
    properties=["1d8 piercing", "Ammunition (range 80/320)", "Loading", "Two-handed"]
)

# Armor
ring_mail = Item(
    name="Ring Mail",
    item_type="Armor",
    cost="30 gp",
    properties=["AC 14", "Disadvantage on Stealth"]
)

breastplate = Item(
    name="Breastplate",
    item_type="Armor",
    cost="400 gp",
    properties=["AC 14", "No disadvantage on Stealth"]
)

hide_armor = Item(
    name="Hide Armor",
    item_type="Armor",
    cost="10 gp",
    properties=["AC 12", "Disadvantage on Stealth"]
)

scale_mail = Item(
    name="Scale Mail",
    item_type="Armor",
    cost="50 gp",
    properties=["AC 14", "Disadvantage on Stealth"]
)

leather_armor = Item(
    name="Leather Armor",
    item_type="Armor",
    cost="10 gp",
    properties=["AC 11", "No disadvantage on Stealth"]
)

chainmail = Item(
    name="Chainmail",
    item_type="Armor",
    cost="75 gp",
    properties=["AC 16", "Strength required: 13", "Disadvantage on Stealth"]
)

plate_armor = Item(
    name="Plate Armor",
    item_type="Armor",
    cost="1500 gp",
    properties=["AC 18", "Strength required: 15", "Disadvantage on Stealth"]
)

shield = Item(
    name="Shield",
    item_type="Shield",
    cost="10 gp",
    properties=["+2 AC", "Held in one hand"]
)

# Additional Armor
studded_leather_armor = Item(
    name="Studded Leather Armor",
    item_type="Armor",
    cost="45 gp",
    properties=["AC 12", "No disadvantage on Stealth"]
)

splint_armor = Item(
    name="Splint Armor",
    item_type="Armor",
    cost="200 gp",
    properties=["AC 17", "Strength required: 15", "Disadvantage on Stealth"]
)

# Adventuring Gear
hammer = Item(
    name="Hammer",
    item_type="Gear",
    cost="1 gp",
    properties=["Useful for driving nails and spikes"]
)

piton = Item(
    name="Piton",
    item_type="Gear",
    cost="5 cp",
    properties=["Used to anchor ropes"]
)

tent = Item(
    name="Tent",
    item_type="Gear",
    cost="2 gp",
    properties=["Shelters up to two people"]
)

crowbar = Item(
    name="Crowbar",
    item_type="Gear",
    cost="2 gp",
    properties=["Provides advantage on Strength checks to break objects"]
)

grappling_hook = Item(
    name="Grappling Hook",
    item_type="Gear",
    cost="2 gp",
    properties=["Useful for climbing"]
)

tinderbox = Item(
    name="Tinderbox",
    item_type="Gear",
    cost="5 sp",
    properties=["Used to light fires"]
)

backpack = Item(
    name="Backpack",
    item_type="Gear",
    cost="2 gp",
    properties=["Can hold up to 30 lbs of gear"]
)

rope = Item(
    name="Rope (50 feet)",
    item_type="Gear",
    cost="1 gp",
    properties=["Made of hemp", "Useful for climbing or securing items"]
)

torch = Item(
    name="Torch",
    item_type="Gear",
    cost="1 cp",
    properties=["Burns for 1 hour", "Provides bright light in a 20-foot radius"]
)

waterskin = Item(
    name="Waterskin",
    item_type="Gear",
    cost="1 gp",
    properties=["Holds 4 pints of liquid"]
)

healer_kit = Item(
    name="Healer's Kit",
    item_type="Gear",
    cost="5 gp",
    properties=["Contains bandages and supplies", "Used to stabilize a dying creature without a Medicine check"]
)

# Additional Adventuring Gear
bedroll = Item(
    name="Bedroll",
    item_type="Gear",
    cost="1 sp",
    properties=["Provides comfort while sleeping outdoors"]
)

lantern = Item(
    name="Lantern",
    item_type="Gear",
    cost="5 gp",
    properties=["Burns for 6 hours on 1 pint of oil", "Provides bright light in a 30-foot radius"]
)

# Magic Items
ring_of_resistance = Item(
    name="Ring of Resistance",
    item_type="Ring",
    cost="6000 gp",
    properties=["Grants resistance to one type of damage"]
)

wand_of_lightning_bolts = Item(
    name="Wand of Lightning Bolts",
    item_type="Wand",
    cost="12000 gp",
    properties=["Casts the Lightning Bolt spell"]
)

cloak_of_invisibility = Item(
    name="Cloak of Invisibility",
    item_type="Wondrous Item",
    cost="15000 gp",
    properties=["Grants the wearer the ability to become invisible"]
)

ring_of_invisibility = Item(
    name="Ring of Invisibility",
    item_type="Ring",
    cost="5000 gp",
    properties=["Grants the wearer the ability to become invisible"]
)

wand_of_magic_missiles = Item(
    name="Wand of Magic Missiles",
    item_type="Wand",
    cost="1000 gp",
    properties=["Casts the Magic Missile spell"]
)

boots_of_elvenkind = Item(
    name="Boots of Elvenkind",
    item_type="Wondrous Item",
    cost="2500 gp",
    properties=["Grants advantage on Dexterity (Stealth) checks"]
)

bag_of_holding = Item(
    name="Bag of Holding",
    item_type="Wondrous Item",
    cost="2000 gp",
    properties=["Holds up to 500 lbs or 64 cubic feet", "Weighs only 15 lbs regardless of contents"]
)

cloak_of_protection = Item(
    name="Cloak of Protection",
    item_type="Wondrous Item",
    cost="1000 gp",
    properties=["Grants +1 bonus to AC and saving throws"]
)

ring_of_protection = Item(
    name="Ring of Protection",
    item_type="Ring",
    cost="2000 gp",
    properties=["Grants +1 bonus to AC and saving throws"]
)
potion_of_greater_healing = Item(
    name="Potion of Greater Healing",
    item_type="Consumable",
    cost="150 gp",
    properties=["Restores 4d4+4 hit points"]
)

potion_of_fire_breath = Item(
    name="Potion of Fire Breath",
    item_type="Consumable",
    cost="300 gp",
    properties=["Allows the user to exhale fire, dealing 4d6 fire damage"]
)

potion_of_invisibility = Item(
    name="Potion of Invisibility",
    item_type="Consumable",
    cost="500 gp",
    properties=["Grants invisibility for 1 hour or until the user attacks or casts a spell"]
)

scroll_of_magic_missile = Item(
    name="Scroll of Magic Missile",
    item_type="Consumable",
    cost="50 gp",
    properties=["Casts the Magic Missile spell once (1st level spell)"]
)

scroll_of_cure_wounds = Item(
    name="Scroll of Cure Wounds",
    item_type="Consumable",
    cost="75 gp",
    properties=["Casts the Cure Wounds spell once (1st level spell)"]
)

potion_of_healing = Item(
    name="Potion of Healing",
    item_type="Consumable",
    cost="50 gp",
    properties=["Restores 2d4+2 hit points"]
)

scroll_of_fireball = Item(
    name="Scroll of Fireball",
    item_type="Consumable",
    cost="200 gp",
    properties=["Casts the Fireball spell once (3rd level spell)"]
)

# Additional Magic Items
boots_of_speed = Item(
    name="Boots of Speed",
    item_type="Wondrous Item",
    cost="3000 gp",
    properties=["Grants the wearer increased speed"]
)

amulet_of_health = Item(
    name="Amulet of Health",
    item_type="Wondrous Item",
    cost="4000 gp",
    properties=["Increases the wearer's Constitution"]
)

core_items = [
    longsword, dagger, greatsword, shortbow, battleaxe, mace, spear, crossbow, warhammer, rapier, longbow, handaxe, morningstar, scimitar,  # Weapons
    leather_armor, chainmail, plate_armor, shield, studded_leather_armor, splint_armor, hide_armor, scale_mail, ring_mail, breastplate,  # Armor
    backpack, rope, torch, waterskin, healer_kit, bedroll, lantern, crowbar, grappling_hook, tinderbox, hammer, piton, tent,  # Adventuring Gear
    bag_of_holding, cloak_of_protection, ring_of_protection, boots_of_speed, amulet_of_health, ring_of_invisibility, wand_of_magic_missiles, boots_of_elvenkind, ring_of_resistance, wand_of_lightning_bolts, cloak_of_invisibility,  # Magic Items
    potion_of_healing, scroll_of_fireball, potion_of_greater_healing, potion_of_fire_breath, potion_of_invisibility, scroll_of_magic_missile, scroll_of_cure_wounds  # Consumables
]