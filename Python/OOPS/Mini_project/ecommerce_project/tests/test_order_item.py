from models.order_item import OrderItem

def test_order_item_total_price():
    order_item = OrderItem('Laptop',50000,2)

    assert order_item.total_price == 100000