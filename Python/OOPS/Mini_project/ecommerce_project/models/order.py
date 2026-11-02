from dataclasses import dataclass, field

from models.order_item import OrderItem


@dataclass
class Order:
    order_id: int
    customer_name: str
    _items: list[OrderItem] = field(default_factory=list)    

    status: str = field(default="pending", init=False)
    total_amount: float = field(default=0, init=False)

    @property
    def items(self):
        return self._items.copy()

    @property
    def total_amount(self) -> float:
        return sum(item.total_price for item in self._items)
    
    def add_item(self, item: OrderItem):
        self._items.append(item)
        self.calculate_total()

    
    def remove_item(self, product_name: str) -> bool:
        original_count = len(self._items)

        self._items = [
            item for item in self._items
            if item.product_name != product_name
        ]

        removed = len(self._items) < original_count

        if removed:
            self.calculate_total()

        return removed
    
    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        
        if new_quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        for item in self._items:
            if item.product_name == product_name:

                if item.quantity == new_quantity:
                    return False

                item.quantity = new_quantity
                self.calculate_total()
                
                return True

        return False

