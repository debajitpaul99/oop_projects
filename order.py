class Order:
    def __init__(self):
        self.orders = {}
    def add_order(self,item):
        if item in self.orders:
            self.orders[item] += item.quantity
        else:
            self.orders[item] = item.quantity
    # def remove_order(self,item_name):
    #     if item_name in self.orders:
    #         del self.orders[item_name]
    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.orders.items())
    def clear(self):
        self.orders = {}