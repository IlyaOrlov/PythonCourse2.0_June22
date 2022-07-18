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
        print("  Издает звук: кря-кря-кря")

    @classmethod
    def colors(cls):
        print(f'  Цвет- {cls.color}')

    def __repr__(self):
        return print(f'Информация об утке:\n  Имя- {self.duck_name} Вес - {self.duck_weight}')

    def __lt__(self, other):
        if self.duck_weight < other.duck_weight:
            return other.duck_name
        else:
            return self.duck_name

    def __ne__(self, other):
        return self.duck_weight != other.duck_weight

    def __add__(self, other):
        return self.duck_weight + other.duck_weight


duck1 = Duck('Donald', 25)
duck2 = Duck('Krek', 30)


lst_duck = [duck1, duck2]

for i in lst_duck:
    info  =  i.__repr__()
    crack_inf = i.crack()
    color_inf = i.colors()


print(f'=====================\n какая утка больше весит? - {duck1.__lt__(duck2)}')
print(f' вес уток не равен? - {duck1.__ne__(duck2)}')
print(f' суммарный вес уток равен = {duck1.__add__(duck2)}')
