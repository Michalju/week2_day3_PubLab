import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Billy", 200)

    #@unittest.skip("Delete this line to run the test")
    def test_person_being_created(self):
        self.assertEqual(self.customer.name, "Billy")
        self.assertEqual(self.customer.wallet, 200)
        self.assertNotEqual(self.customer.wallet, 100)