from models.order_status import OrderStatus
from models.order_item import OrderItem
from models.order import Order


class OrderService:
    def __init__(self, order: Order):
        self.order = order
        
    def add_item(self, item: OrderItem) -> None:
        self.order.add_item(item)
        
    def remove_item(self, product_name: str) -> bool:
        return self.order.remove_item(product_name)
    
    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        return self.order.update_quantity(product_name,new_quantity)
    
    def calculate_total(self) -> float:
        return self.order.total_amount
    
    def pay_order(self) -> None:
        self.order.change_status(OrderStatus.PAID)
    
    def cancel_order(self) -> None:
        self.order.change_status(OrderStatus.CANCELLED)
    