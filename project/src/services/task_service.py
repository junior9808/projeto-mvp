from models.task import Order

class TaskService:
    def __init__(self):
        self.orders = []

    def create_order(self, customer: str, product: str):
        order = Order(len(self.orders) + 1, customer, product)
        self.orders.append(order)
        return order

    def list_orders(self):
        return self.orders

    def complete_order(self, order_id: int):
        for order in self.orders:
            if order.id == order_id:
                order.status = "entregue"
                return order
        return None

    def delete_order(self, order_id: int):
        for order in self.orders:
            if order.id == order_id:
                self.orders.remove(order)
                return True
        return False