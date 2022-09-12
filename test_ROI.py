import unittest
from ROI import User, ROI, User_interface

class TestCart(unittest.TestCase):

    def create_user(self):
        test_create_user = ROI()

        test_create_user('victor', 'property1', 'income1', 3000, 'expense1', 1200, 'Investment1', 60000)
        self.assertIn('victor', test_create_user.items)
        self.assertEqual(test_create_user.items['victor'].income_amount, 3000)

if __name__ == '__main__':
    unittest.main()