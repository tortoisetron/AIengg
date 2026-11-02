from models.order import Order
from models.order_item import OrderItem

item1 = OrderItem("Laptop", 50000, 2)
item2 = OrderItem("Mouse", 50000, 2)
item3 = OrderItem("Keyboard", 500, 1)

# order = Order(
#     order_id=101,
#     customer_name="Rahul",
#     # items=[item1,item2]
# )

# order.items.append("Apple")


# # print(order.items)
order = Order(
    order_id=101,
    customer_name="Rahul",
)
order.add_item(OrderItem("Laptop", 50000, 1))
order.add_item(OrderItem("Mouse", 500, 2))
order.add_item(OrderItem("Keyboard", 2000, 1))

# order.remove_item('Laptop')
print(order.update_quantity('Laptop',5))




print(order.total_amount)




