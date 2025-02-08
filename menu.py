class Menu:
    def __init__(self):
        self.items = []
    def add_item(self,item):
        self.items.append(item)
    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print('Item deleted')
        else:
            print('Item not found')
    def view_items(self):
        print('***Available items***')
        for item in self.items:
            print(f'Name:{item.name}\tPrice:{item.price}\tQuantity:{item.quantity}')