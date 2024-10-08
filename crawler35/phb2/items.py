class Item:
    def __init__(self, name, item_type, cost, properties):
        self.name = name
        self.item_type = item_type
        self.cost = cost
        self.properties = properties

# Psionic Items

mind_blade = Item(
    name="Mind Blade",
    item_type="Weapon (Psionic)",
    cost="10,000 gp",
    properties=["1d8 psychic damage", "Can channel psionic energy"]
)

cognizance_crystal = Item(
    name="Cognizance Crystal",
    item_type="Psionic Item",
    cost="3,000 gp",
    properties=["Stores up to 5 power points", "Can be used to replenish psionic powers"]
)

# Add the new psionic items to the list
phb2_items = [mind_blade, cognizance_crystal]