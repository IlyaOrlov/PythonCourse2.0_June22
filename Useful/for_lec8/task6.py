class Employee:
    def __init__(self, name, surname, salary):
        self._name = name
        self._surname = surname
        self._salary = salary

    def show_employee(self):
        print(f"I'm {self._name} {self._surname} with {self._salary}")

    def increase_salary(self, bonus):
        self._salary += bonus


class Manager(Employee):
    def __init__(self, name, surname, salary, employees):
        super().__init__(name, surname, salary)
        self.employees = employees

    def show_employee(self):
        print(f"I'm {self._name} {self._surname} with {self._salary} and {self.employees}")

    def show_manager(self):
        super().show_employee()

    def show_employees(self):
        print(self.employees)


e1 = Employee('Ivan', 'Ivanov', 100000)
m1 = Manager('Victor', 'Victorov', 150000, [])
m1.show_manager()
m1.increase_salary(2000)
m1.show_manager()
lst = [e1, m1]
for i in lst:
    i.show_employee()