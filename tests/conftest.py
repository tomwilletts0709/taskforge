class FakeOrderRepo: 
    def __init__(self): 
        self.orders = {}

    def create_order(self, order): 
        self.orders[order.id] = order 
        return order 
    
    def get_order(self, order_id): 
        return self.orders.get(order_id)
    
    def delete_order(self, order_id): 
        if order_id not in self.orders: 
            return False
        
        del self.orders[order_id]
        return True
    
    def list_orders(self): 
        return list(self.orders.values())