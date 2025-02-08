from menu import Menu

class Restaurant:
    def __init__(self,name):
        self.name = name
        self.employees = []
        self.menu = Menu()
    def add_employee(self, employee):
        self.employees.append(employee)
    def view_employees(self):
        for emp in self.employees:
            print(f'Name:{emp.name}\nDesignation:{emp.designation}\nAddress:{emp.address}')
    def remove_employee(self,employee_id):
        for emp in self.employees:
            if emp.id == employee_id:
                self.employees.remove(emp)
                break
