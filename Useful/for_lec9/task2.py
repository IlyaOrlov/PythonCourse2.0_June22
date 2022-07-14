class Pizza:
    def make_base(self):
        print('make base')

    def add_ingr(self):
        print('add ingr')

    def bake(self):
        print('bake')


class VegPizza(Pizza):
    def add_ingr(self):
        print('add vegetables')


class MushPizza(Pizza):
    def add_ingr(self):
        print('add mushrooms')


class MeatPizza(Pizza):
    def add_ingr(self):
        print('add meat')


def make_pizza(pizza):
    pizza.make_base()
    pizza.add_ingr()
    pizza.bake()


lst = [VegPizza(), MushPizza(), MeatPizza()]
for p in lst:
    make_pizza(p)