from dataclasses import dataclass, field
from datetime import datetime
from models.order_history import OrderHistory
from models.order_item import OrderItem
import copy
from models.order_status import ALLOWED_TRANSITIONS, OrderStatus

@dataclass
class Order:
    order_id: int
    customer_name: str
    _items: list[OrderItem] = field(default_factory=list)    

    _status: OrderStatus = field(
        default=OrderStatus.PENDING,
        init=False,
        repr=False
    )
    _history: list[OrderHistory] = field(
        default_factory=list,
        repr=False
    )
    
    def __post_init__(self):
        self._record_status_change(self.status)

    @property
    def items(self):
        return self._items.copy()
    
    @property
    def status(self) -> OrderStatus:
        return self._status
    
    @property
    def history(self) -> list[OrderHistory]:
        return copy.deepcopy(self._history)

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
    
    def change_status(self, new_status: OrderStatus) -> None:

        if not isinstance(new_status, OrderStatus):
            raise TypeError("Status must be an OrderStatus")

        allowed = ALLOWED_TRANSITIONS[self._status]
        
        if new_status == OrderStatus.PAID:
            if not self._items:
                raise ValueError("Cannot pay for an empty order")
        
        if new_status == OrderStatus.CANCELLED:
            if self._status in (OrderStatus.SHIPPED, OrderStatus.DELIVERED):
                raise ValueError(f'order is already {self._status.value}')
            

        if new_status not in allowed:
            raise ValueError(
                f"Cannot change status from "
                f"{self._status.value} to {new_status.value}"
            )
        self._status = new_status
        self._record_status_change(new_status)
        
    def _record_status_change(self, status: OrderStatus):
        
        self._history.append(OrderHistory(status,datetime.now()))
    

