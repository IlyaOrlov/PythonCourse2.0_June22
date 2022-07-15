class HeroExceptionError(Exception):
    pass


class Hero:
    def __init__(self, power):
        self._power = power

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        if isinstance(value, int):
            self._power = value
        else:
            raise HeroExceptionError('Bad power')

    def __add__(self, other):
        return Hero(self.power + other.power)


h1 = Hero(10)
h2 = Hero(30)
#h.power = '200'
print(h1.power)
print(h2.power)
h = h1 + h2
h2.power = '200'
print(h.power)
