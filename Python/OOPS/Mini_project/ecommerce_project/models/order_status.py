from enum import Enum

class OrderStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    
    
ALLOWED_TRANSITIONS = {
    OrderStatus.PENDING: [
        OrderStatus.PAID,
        OrderStatus.CANCELLED
    ],
    OrderStatus.PAID: [
        OrderStatus.PROCESSING,
        OrderStatus.CANCELLED
    ],
    OrderStatus.PROCESSING: [
        OrderStatus.SHIPPED
    ],
    OrderStatus.SHIPPED: [
        OrderStatus.DELIVERED
    ],
    OrderStatus.DELIVERED: [],
    OrderStatus.CANCELLED: []
}
