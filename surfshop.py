class TooManyBoardsError(Exception):
    pass

class ShoppingCart():
    def __init__(self):
        self.num_surfboards = 0
        self.locals_discount = True

    def add_surfboards(self,quantity=1):
        if self.num_surfboards + quantity > 4:
            raise TooManyBoardsError
        else:
            self.num_surfboards += quantity
            suffix = "" if quantity == 1 else "s"
            return f"Successfully added {quantity} surfboard{suffix} to your cart!"

    def apply_locals_discount(self):
        pass



























