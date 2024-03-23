class TooManyBoardsError(Exception):
    def __str__(self):
        return("Cannot have more than 4 surfboards in basket")


class ShoppingCart():
    def __init__(self):
        self.num_surfboards = 0
        self.locals_discount = False

    def add_surfboards(self,quantity=1):
        if self.num_surfboards + quantity > 4:
            raise TooManyBoardsError
        else:
            self.num_surfboards += quantity
            suffix = "" if quantity == 1 else "s"
            return f"Successfully added {quantity} surfboard{suffix} to your cart!"

    def apply_locals_discount(self):
        pass

a1 = ShoppingCart()
print(a1.add_surfboards(4))

























