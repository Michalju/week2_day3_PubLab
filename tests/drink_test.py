import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Guinness", 10)

    #@unittest.skip("Delete this line to run the test")
    def test_create_first_drink(self):
        self.assertEqual(self.drink_1.name, "Guinness")
        self.assertEqual(self.drink_1.price, 10)
        self.assertNotEqual(self.drink_1.price, 20)