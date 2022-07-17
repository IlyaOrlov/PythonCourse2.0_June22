class Tank:
    def __init__(self):
        self.speed = 300
        self.power = 500

    def shoot(self):
        print('Ba-bah')


class T34(Tank):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.speed = 1.5 * self.speed

    def shoot(self):
        print('T34: Ba-bah')

    def super_shoot(self):
        super().shoot()
        print('T34: super_shoot')


class Tiger:
    def shoot(self):
        print('Bah')


class Abrams:
    def shoot(self):
        print('Super bah')


t34 = T34('grey')
tg = Tiger()
t_ab = Abrams()

print(t34.speed, t34.color)
t34.shoot()
t34.super_shoot()

lst = [t34, tg, t_ab]
for t in lst:
    t.shoot()
