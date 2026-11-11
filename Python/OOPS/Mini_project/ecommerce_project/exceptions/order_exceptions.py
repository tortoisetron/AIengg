class OrderError(Exception):
    pass

class EmptyOrderError(OrderError):
    pass

class InvalidOrderStatusError(OrderError):
    pass

class ProductNotFoundError(OrderError):
    pass