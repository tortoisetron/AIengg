from exceptions.order_exceptions import EmptyOrderError, ProductNotFoundError
from services.order_service import OrderService
from models.order import Order
from models.order_status import OrderStatus
from models.order_item import OrderItem

order = Order(101, "Alice")

order_svc = OrderService(order)

order_svc.add_item(OrderItem("Laptop", 50000, 1))
order_svc.add_item(OrderItem("mouse", 5000, 2))

print(order_svc.calculate_total())
try:
    order_svc.pay_order()
except EmptyOrderError as e:
    print(e)

print(order.status)
for status in order.history:
    print(f'status: {status.status.value} , time: {status.timestamp}')


try:
    order_svc.remove_item('keyboard')
except ProductNotFoundError as e:
    print(e)
    