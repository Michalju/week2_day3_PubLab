import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Guinness", 10)
        self.drink_2 = Drink("Gin", 15)
        self.drink_3 = Drink("Whisky", 20)
        self.BrewDog = Pub("Brewdog_edinburgh", 100, [self.drink_1, self.drink_2, self.drink_3])


    #@unittest.skip("Delete this line to run the test")
    def test_create_first_pub(self):
        self.assertEqual(self.BrewDog.name, "Brewdog_edinburgh")
        self.assertEqual(self.BrewDog.till, 100)
        self.assertNotEqual(self.BrewDog.till, 200)
        self.assertEqual(len(self.BrewDog.drinks), 3)
        