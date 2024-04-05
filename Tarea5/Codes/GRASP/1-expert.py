class Order:
    def __init__(self, order_id, customer, total_amount):
        self.order_id = order_id
        self.customer = customer
        self.total_amount = total_amount


class OrderProcessor:
    def process_order(self, order):
        print(
            f"Procesando pedido {order.order_id} para el cliente {order.customer}")
        print(f"Total a pagar: ${order.total_amount}")


order = Order(1, "John Doe", 100)
processor = OrderProcessor()
processor.process_order(order)
