from enum import Enum


class OrderStatus(Enum):
    NEW  = 1
    PAID = 2
    SHIPPED = 3


def print_status(status: OrderStatus):
    print(f'Статус заказа: {status.name}')

print_status(OrderStatus.NEW)