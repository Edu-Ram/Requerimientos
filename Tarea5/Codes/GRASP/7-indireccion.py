class PaymentGateway:
    def process_payment(self, amount):
        print(f"Procesando pago por ${amount}")


class PaymentProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def process_payment(self, amount):
        self.payment_gateway.process_payment(amount)


payment_gateway = PaymentGateway()
payment_processor = PaymentProcessor(payment_gateway)
payment_processor.process_payment(100)
