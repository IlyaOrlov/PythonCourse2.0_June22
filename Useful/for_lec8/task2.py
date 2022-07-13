class Employee:
    what = 'employee'

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name
        self.salary = 100000

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return f"{self.first_name} {self.last_name} with {self.salary}"

    def say_my_name(self):
        print(f"say_my_name: I'm {self.first_name} {self.last_name}")

    @classmethod
    def what_is(cls):
        print(cls.what)

    @staticmethod
    def say_hello():
        print('Hell!')


e1 = Employee('Petr', 'Petrov')
e2 = Employee('Semen', 'Semenov')
e1.say_my_name()
e3 = Employee('Victor', 'Victorov')
Employee.say_hello()
e1.say_hello()

print(e1)
# e1.first_name = 'Petr'
# e1.last_name = 'Petrov'
#
# e1.say_my_name()
# e2.say_my_name()
# Employee.say_my_name(e1)
# print(e1.__dict__)
# print(e1.first_name, e1.last_name)
# print(e2.first_name, e2.last_name)

# e1.first_name = 'Petr'
# e1.last_name = 'Petrov'
# print(e1.__dict__)
# print(Employee.__dict__)
# e2.first_name = 'Semen'
# e2.last_name = 'Semenov'
# print(e1.first_name, e1.last_name)
# print(e2.first_name, e2.last_name)
# print(Employee.first_name, Employee.last_name)
# print(e1.__dict__)
# print(Employee.__dict__)