'''1. Спроектировать классы (один или несколько) для игры в танки и создать экземпляры этих классов.'''

class Tank:
    color = "Green"

    def __init__(self, power, speed):
        self.power = power
        self.speed = speed

    @staticmethod
    def move():
        print("Танка поехал.")

    @staticmethod
    def shoot():
        print("Танка выстрелил.")


t1 = Tank(500, 70)
t2 = Tank(300, 100)
t1.move()
t2.shoot()
print(Tank.color)

'''2. Спроектировать класс Duck, при создании экземпляров которого будут задаваться атрибуты name, weight, 
а атрибут color должен быть общим для всех экземпляров класса. Также в классе должны быть методы:
- статический метод, выводящий «Сrack»;
- классовый метод, выводящий цвет уток;
- методы экземпляров: метод, выводящий имя и вес утки; метод __repl__ ; метод, принимающий 2х уток, и возвращающий 
имя более тяжелой утки (__lt__); метод, сравнивающий вес 2х уток и возвращающий bool (равен вес или нет (__ne__)); 
метод, суммирующий вес 2х уток(__add__).
'''

class Duck:
    color = "White"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def crack():
        print("Crack!")

    @classmethod
    def colors(cls):
        print(cls.color)

    def __repr__(self):
        return f'Эту утку зовут {self.name}, ее цвет {self.color}, ее вес {self.weight}'

    def __ne__(self, other):
        return self.weight != other.weight

    def __lt__(self, other):
        # _a = self.weight < other.weight
        # return self.name
        if self.weight < other.weight:
            return other.name
        else:
            return self.name

    def __add__(self, other):
        return self.weight + other.weight


d1 = Duck("Donald", 50)
d1.colors()
d2 = Duck("Daisy", 30)
d2.crack()
ducks = (d1, d2)
for i in ducks:
    print(i)
print(f"Утки разного веса?\n- {d1 != d2}")
print(f"Какая утка весит больше?\n- {d1 < d2}")
print(f"А сколько весят обе утки?\n- {d1 + d2}")
