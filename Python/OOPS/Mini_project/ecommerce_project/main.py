from models.order import Order
from models.order_item import OrderItem

order = Order(101, "Alice")

order.add_item(OrderItem("Laptop", 50000, 1))
order.add_item(OrderItem("Mouse", 500, 2))

print(order.total_amount)
# 51000

order.update_quantity("Laptop", 2)

print(order.total_amount)
# 101000

order.remove_item("Mouse")

print(order.total_amount)
# 100000





