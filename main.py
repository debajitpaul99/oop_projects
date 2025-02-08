from food_item import FoodItem
from menu import Menu
from user import Customer, Admin, Employee
from restaurant import Restaurant
from order import Order

tct = Restaurant('Teracotta')
def customer_menu():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone: ')
    address = input('Enter address: ')
    customer = Customer(name=name,email=email,phone=phone,address=address)

    while True:
        print(f'Welcome {customer.name}!!')
        print('1. View menu')
        print('2. Add item to cart')
        print('3. view cart')
        # print('4. Remove from cart')
        print('4. Pay bill')
        print('5. Exit')
        op = int(input('Choose an option: '))
        if op == 1:
            customer.view_menu(tct)
        elif op == 2:
            item_name = input('Enter item name: ')
            quantity = int(input('Enter quantity: '))
            customer.add_to_cart(tct,item_name,quantity)
        elif op == 3:
            customer.view_cart()
        # elif op == 4:
        #     item = input('Enter item name: ')
        #     customer.remove_from_cart(item)
        elif op == 4:
            customer.pay_bill()
        elif op == 5:
            break
        else:
            print(f'Invalid option!!!')

def admin_menu():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone: ')
    address = input('Enter address: ')
    admin = Admin(name=name,email=email,phone=phone,address=address)

    while True:
        print(f'Welcome {admin.name}!!')
        print('1. Add employee')
        print('2. View Employee')
        print('3. Remove employee')
        print('4. Add new item')
        print('5. Remove item')
        print('6. View menu')
        print('7. Exit')
        op = int(input('Choose an option: '))
        if op == 1:
            name = input('Enter employee name: ')
            email = input('Enter email: ')
            phone = input('Enter phone: ')
            address = input('Enter address: ')
            age = int(input('Enter age: '))
            designation = input('Designation: ')
            salary = input('Salary: ')
            id = input('Employee ID: ')
            employee = Employee(name=name,email=email,phone=phone,address=address,age=age,designation=designation,salary=salary,id=id)
            admin.add_employee(tct,employee)
        elif op == 2:
            admin.view_employees(tct)
        elif op == 3:
            id = input('Enter employee ID to remove: ')
            admin.remove_employee(tct,id)
        elif op == 4:
            name = input('Enter food name: ')
            price = int(input('Enter price: '))
            quantity = int(input('Quantity: '))
            item = FoodItem(name=name,price=price,quantity=quantity)
            admin.add_new_item(tct,item)
        elif op == 5:
            item_name = input('Enter food name: ')
            admin.remove_item(tct,item_name)
        elif op == 6:
            admin.view_menu(tct)
        elif op == 7:
            break
        else:
            print(f'Invalid option!!!')

while True:
    print('Welcome!!!')
    print('1. Customer')
    print('2. Admin')
    print('3. Exit')
    op = int(input('Choose an option: '))
    if op == 1:
        customer_menu()
    elif op == 2:
        admin_menu()
    elif op == 3:
        break
    else:
        print(f'Invalid option!!!')