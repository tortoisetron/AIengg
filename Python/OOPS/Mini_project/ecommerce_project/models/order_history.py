from dataclasses import dataclass
from datetime import datetime
from models.order_status import OrderStatus

@dataclass(frozen=True)
class OrderHistory:
    status: OrderStatus 
    timestamp: datetime