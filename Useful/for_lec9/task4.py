class Employee:
    def __init__(self, name, suname):
        if isinstance(name, str) and isinstance(suname, str):
            self.name = name
            self.suname = suname
        else:
            print('Error')
            raise Exception


e1 = Employee(100, 200)
print('----')
print(e1.name, e1.suname)
