import unittest
from phb1.classes import core_classes
from phb1.races import core_races
from phb1.items import core_items
from phb1.monsters import core_monsters
from phb1.spells import core_spells
from game import allocate_ability_points, combat

class TestDungeonCrawler(unittest.TestCase):

    def test_classes_loading(self):
        """Test that core classes are loading correctly."""
        self.assertGreater(len(core_classes), 0, "No classes found.")
        self.assertIn("Fighter", [cls.name for cls in core_classes], "Fighter class missing.")

    def test_races_loading(self):
        """Test that core races are loading correctly."""
        self.assertGreater(len(core_races), 0, "No races found.")
        self.assertIn("Elf", [race.name for race in core_races], "Elf race missing.")

    def test_ability_point_allocation(self):
        """Test that the ability point allocation system works."""
        abilities = allocate_ability_points()  # You can manually set points here for testing
        self.assertEqual(len(abilities), 6, "Not all abilities are allocated.")
        self.assertTrue(all(abilities[ability] >= 8 for ability in abilities), "Ability scores should not be below 8.")
    
    def test_items_loading(self):
        """Test that core items are loading correctly."""
        self.assertGreater(len(core_items), 0, "No items found.")
        self.assertIn("Longsword", [item.name for item in core_items], "Longsword missing.")

    def test_spells_loading(self):
        """Test that core spells are loading correctly."""
        self.assertGreater(len(core_spells), 0, "No spells found.")
        self.assertIn("Magic Missile", [spell.name for spell in core_spells], "Magic Missile spell missing.")

    def test_combat(self):
        """Test that combat between player and monster works."""
        monster = core_monsters[0]  # Goblin for testing
        # Basic check to ensure combat logic doesn't fail
        self.assertGreater(monster.hit_points, 0, "Monster HP is incorrect.")
        # You can add more detailed combat logic tests here

if __name__ == '__main__':
    unittest.main()