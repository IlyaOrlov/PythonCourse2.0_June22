# Спроектировать класс Duck, при создании экземпляров которого будут задаваться атрибуты
# name, weight, а атрибут color должен быть общим для всех экземпляров класса.
# Также в классе должны быть методы:
# - статический метод, выводящий «Сrack»;
# - классовый метод, выводящий цвет уток;
# - методы экземпляров: метод, выводящий имя и вес утки;
# метод __repl__ ;
# метод, принимающий 2х уток, и возвращающий имя более тяжелой утки (__lt__) ;
# метод, сравнивающий вес 2х уток и возвращающий bool (равен вес или нет (__ne__)) ;
# метод, суммирующий вес 2х уток(__add__).

class Duck:
    color = 'green'

    def __init__(self, name, weight):
        self.duck_name = name
        self.duck_weight = weight

    @staticmethod
    def crack():
        print("кря-кря-кря")

    @classmethod
    def colors(cls):
        print(cls.color)

    def __repr__(self):
        return f'Duck({self.duck_name}, {self.color}, {self.duck_weight})'

    def __lt__(self, other):
        return self.duck_weight < other.duck_weight

    def __ne__(self, other):
        return self.duck_weight< other.duck_weight

    def __add__(self, other):
        return self.duck_weight + other.duck_weight


duck1 = Duck('Donald', 25)
duck2 = Duck('Krek', 30)


print(f'{duck1.__repr__()} \n {duck2.__repr__()}')
print(duck2.__lt__(duck1))
print(duck2.__ne__(duck1))
print(duck1.__add__(duck2))
