import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Guinness", 10, 2)
        self.drink_2 = Drink("Gin", 15, 4)
        self.drink_3 = Drink("Whisky", 20, 6)
        self.BrewDog = Pub("Brewdog_edinburgh", 100, [self.drink_1, self.drink_2, self.drink_3])
        self.customer = Customer("Billy", 200, 45)
        self.customer_2 = Customer("Jane", 5, 30)
        self.customer_3 = Customer("Gerorge", 50, 16)


    #@unittest.skip("Delete this line to run the test")
    def test_create_first_pub(self):
        self.assertEqual(self.BrewDog.name, "Brewdog_edinburgh")
        self.assertEqual(self.BrewDog.till, 100)
        self.assertNotEqual(self.BrewDog.till, 200)
        self.assertEqual(len(self.BrewDog.drinks), 3)
        

    def test_drink_exists(self):
        self.assertTrue(self.BrewDog.drink_exists("Guinness"))
        self.assertTrue(self.BrewDog.drink_exists("Gin"))
        self.assertTrue(self.BrewDog.drink_exists("Whisky"))
        self.assertFalse(self.BrewDog.drink_exists("Wine"))

    def test_sell_the_drink(self):
        self.BrewDog.sell_the_drink("Gin", self.customer)
        self.assertEqual(self.customer.wallet, 185) 
        self.assertEqual(self.BrewDog.till, 115)
        self.assertEqual(self.customer._drunkenness, 4)
        self.BrewDog.sell_the_drink("Wine", self.customer)
        self.assertEqual(self.customer.wallet, 185) 
        self.assertEqual(self.BrewDog.till, 115)
        self.BrewDog.sell_the_drink("Gin", self.customer_2)
        self.assertEqual(self.customer_2.wallet, 5) 
        self.assertEqual(self.BrewDog.till, 115)
        self.BrewDog.sell_the_drink("Gin", self.customer_3)
        self.assertEqual(self.customer_3.wallet, 50)
        self.assertEqual(self.BrewDog.till, 115)

        
