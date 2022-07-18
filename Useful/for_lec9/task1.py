class Tank:
    def __init__(self, speed, power):
        self._speed = speed
        self._power = power

    def shoot(self):
        pass

    def __lt__(self, other):
        if self._speed == other._speed:
            return self._power < other._power
        return self._speed < other._speed

    def __le__(self, other):
        if self._speed == other._speed:
            return self._power <= other._power
        return self._speed <= other._speed

    def __repr__(self):
        return f"{type(self).__name__}: speed({self._speed}) power({self._power})"

class TankT34(Tank):
    def shoot(self):
        print('Bah')


class TankTiger(Tank):
    def shoot(self):
        print('Ba-bah')


class TankAbroms(Tank):
    def shoot(self):
        print('Ba-ba-bah')


t34 = TankT34(10, 20)
tt1 = TankTiger(30, 40)
tt2 = TankTiger(30, 50)
ta = TankAbroms(50, 60)
lst = [t34, tt2, tt1, ta]
# for t in lst:
#     t.shoot()

lst.sort()
print(lst)
print(tt1 <= tt2)
