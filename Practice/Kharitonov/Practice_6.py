# 1.Спроектировать классы (один или несколько) для игры в танки и создать экземпляры этих классов.
class Tank():
    def __init__(self, name, speed, damag):
        self.name = name
        self.speed = speed

        self.damag = damag

    def show_tank(self):
        print(f'Имя {self.name} Скорость: {self.speed} Урон: {self.damag} ')

    def move(self):
        print("Tank " + self.name + " -> Движение")

    def lev_up(self):
        self.speed += 20
        print(f'Скорость Танка {self.name} +20 = {self.speed}')


tank_1 = Tank('ИСУ-152', 40, 100)
tank_2 = Tank('CY-100', 60, 70)


tank_1.show_tank()
tank_2.show_tank()
tank_1.move()
tank_2.move()
tank_2.lev_up()
tank_1.lev_up()

# Спроектировать класс Duck, при создании экземпляров которого будут задаваться атрибуты name, weight,
# а атрибут color должен быть общим для всех экземпляров класса. Также в классе должны быть методы:
# - статический метод, выводящий «Сrack»;
# - классовый метод, выводящий цвет уток;
# - методы экземпляров: метод, выводящий имя и вес утки;
# метод __repl__ ; метод, принимающий 2х уток, и возвращающий имя более тяжелой утки (__lt__) ;  метод,
# сравнивающий вес 2х уток и возвращающий bool (равен вес или нет (__ne__)) ; метод, суммирующий вес 2х уток(__add__).

class Duck:
    color = 'Черный'

    def __init__(self, name, weight):
        self.duck_name = name
        self.duck_weight = weight

    @staticmethod
    def crack():
        print('«Сrack»')

    @classmethod
    def colors(cls):
        print(f'Цвет утки -> {cls.color}')

    def __repr__(self):
        return (f'Имя утки -> {self.duck_name}  Вес -> {self.duck_weight}')

    def __lt__(self, other):
        if self.duck_weight < other.duck_weight:
            return other.duck_name
        else:
            return self.duck_name

    def __ne__(self, other):
        return self.duck_weight != other.duck_weight

    def __add__(self, other):
        return self.duck_weight + other.duck_weight


duck_1 = Duck('Кряка', 5)
duck_2 = Duck('Даки', 3)
totl_duck = [duck_1, duck_2]
for i in totl_duck:
    print(i)
    i.crack()
    i.colors()


print(f'Утка с большим весом -> {duck_1 < duck_2}')
print(f'Равен ли вес уток -> {duck_1 != duck_2}')
print(f'Суммарный вес 2х уток = {duck_1 + duck_2}')