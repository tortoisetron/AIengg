from dataclasses import dataclass, field
from models.order_item import OrderItem

@dataclass
class Order:
    order_id: int
    customer_name: str
    _items: list[OrderItem] = field(default_factory=list)    

    status: str = field(default="pending", init=False)
    # total_amount: float = field(default=0, init=False)

    @property
    def items(self):
        return self._items.copy()

    @property
    def total_amount(self) -> float:
        return sum(item.total_price for item in self._items)
    
    def add_item(self, item: OrderItem):
        if not isinstance(item, OrderItem):
            raise TypeError("Expected an OrderItem object")
        self._items.append(item)

    
    def remove_item(self, product_name: str) -> bool:
        original_count = len(self._items)

        self._items = [
            item for item in self._items
            if item.product_name != product_name
        ]

        return len(self._items) < original_count
    
    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        
        if new_quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        for item in self._items:
            if item.product_name == product_name:

                if item.quantity == new_quantity:
                    return False

                item.quantity = new_quantity                
                return True

        return False

