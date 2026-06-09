class Order:
    def __init__(self, id, customer, product):
        self.id = id
        self.customer = customer
        self.product = product
        self.status = "pendente"