class Employee:
    def __init__(self, name, surname, salary):
        self._name = name
        self._surname = surname
        self._salary = salary

    def show_employee(self):
        print(f"I'm {self._name} {self._surname} with {self._salary}")

    @property
    def salary(self):  # e.salary
        return self._salary

    @salary.setter  # e.salary = 2000
    def salary(self, bonus):
        if self._salary + bonus < 0:
            print('Incorrect bonus')
        else:
            self._salary += bonus

    @salary.deleter
    def salary(self):
        print('Salary deleted')


e1 = Employee('Ivan', 'Ivanov', 100000)
print(e1.salary)
e1.salary = -300000
print(e1.salary)
del e1.salary

