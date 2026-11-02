from dataclasses import dataclass, field


@dataclass
class OrderItem:
    product_name: str
    unit_price: float
    quantity: int

    total_price: float = field(init=False)

    def __post_init__(self):
        if self.unit_price < 0:
            raise ValueError("Price cannot be negative")

        if self.quantity <= 0:
            raise ValueError("Quantity must be positive")

        self.total_price = self.unit_price * self.quantity