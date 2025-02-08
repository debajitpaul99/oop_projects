from abc import ABC
from order import Order

class User(ABC):
    def __init__(self,name,email,phone,address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class Customer(User):
    def __init__(self, name, email, phone, address):
        self.cart = Order()
        super().__init__(name, email, phone, address)
    def view_menu(self,restaurant):
        restaurant.menu.view_items()
    def add_to_cart(self,restaurant,item_name,quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if item.quantity >= quantity:
                item.quantity = quantity
                self.cart.add_order(item)
                print('Item added')
            else:
                print('Item quantity exceeded!!!')
        else:
            print('Item not found')
    def view_cart(self):
        print('***Ordered Menu***')
        for item,quantity in self.cart.orders.items():
            print(f'Name:{item.name}\tPrice:{item.price}\tQuantity:{quantity}')
        print(f"Total price:{self.cart.total_price()} tk")
    def remove_from_cart(self,item_name):
        self.cart.orders.remove_order(item_name)
        print('Item removed')
    def pay_bill(self):
        print(f'Total {self.cart.total_price()} tk paid sucessfully. Thank you.')
        self.cart.clear()

class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary, id):
         self.age = age
         self.designation = designation
         self.salary = salary
         self.id = id
         super().__init__(name, email, phone, address)

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)
        print(f'Employee {employee.name} added...')
    def view_employees(self,restaurant):
        print('---Employee List----')
        restaurant.view_employees()
    def remove_employee(self,restaurant,employee_id):
        restaurant.remove_employee(employee_id)
        print(f'{employee_id} Employee ID removed successfully')
    def add_new_item(self,restaurant,item):
        restaurant.menu.add_item(item)
    def remove_item(self,restaurant,item):
        restaurant.menu.remove_item(item)
    def view_menu(self,restaurant):
        restaurant.menu.view_items()
        