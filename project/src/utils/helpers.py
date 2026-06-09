def format_order(order):
    return {
        "id": order.id,
        "cliente": order.customer,
        "produto": order.product,
        "status": order.status
    }

def filter_completed(orders):
    return [o for o in orders if o.status == "entregue"]