class OrderItem:
    def __init__(self, product_name, unit_price, quantity):
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
            raise ValueError("Quantity must be a positive integer")
        self._quantity = value

    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._unit_price = value

    @property
    def total_price(self):
        return self.unit_price * self.quantity