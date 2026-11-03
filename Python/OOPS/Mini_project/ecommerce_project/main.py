from models.order import Order
from models.order import OrderStatus
from models.order_item import OrderItem


# order = Order(101, "Alice")

# order.add_item(OrderItem("Laptop", 50000, 1))
# order.add_item(OrderItem("Mouse", 500, 2))

# print(order.total_amount)
# # 51000

# order.update_quantity("Laptop", 2)

# print(order.total_amount)
# # 101000

# order.remove_item("Mouse")

# print(order.total_amount)
# # 100000

# status = OrderStatus.PENDING

# print(status)
# # OrderStatus.PENDING

# print(status.value)
# # pending

# print(status.name)
# # PENDING


order = Order(101, "Alice")

# print(order.status)
# OrderStatus.PENDING
order.add_item(OrderItem("Laptop", 50000, 1))
order.change_status(OrderStatus.PAID)
order.change_status(OrderStatus.PROCESSING)
order.change_status(OrderStatus.SHIPPED)
order.change_status(OrderStatus.DELIVERED)
# order.change_status(OrderStatus.CANCELLED)
# order.history[0]["status"] = OrderStatus.DELIVERED

previous_count = len(order.history)

try:
    order.change_status(OrderStatus.CANCELLED)
except ValueError as e:
    print(e)

print(len(order.history) == previous_count)
# for status in order.history:
#     print(f'status: {status.status.value} , time: {status.timestamp}')

# print(order.history)

# OrderStatus.PAID

# order.change_status(OrderStatus.PAID)

# OrderStatus.PROCESSING