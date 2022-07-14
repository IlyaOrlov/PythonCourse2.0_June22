# Написать класс Man, который принимает имя в конструкторе.
# Имеет метод solve_task, который просто выводит "I'm not ready yet".


class Man:
    def __init__(self, name):
        self.man_name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")


mans_1 = Man("Igor")


print(mans_1.man_name)
mans_1.solve_task()
