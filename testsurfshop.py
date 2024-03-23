import surfshop
import unittest

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_surfboard(self):
        message = self.cart.add_surfboards(quantity=1)
        self.assertEqual(message,"Successfully added 1 surfboard to your cart!")

    def test_add_surfboards(self):
        for i in range(2,5):
            with self.subTest(i):
                message = self.cart.add_surfboards(quantity=i)
                self.assertEqual(message,f"Successfully added {i} surfboards to your cart!")
                self.cart = surfshop.ShoppingCart()

    def test_too_many_boards(self):
        self.assertRaises(surfshop.TooManyBoardsError,self.cart.add_surfboards,5)

    @unittest.expectedFailure
    def test_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

unittest.main()