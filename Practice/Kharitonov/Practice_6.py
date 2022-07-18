# 1.Спроектировать классы (один или несколько) для игры в танки и создать экземпляры этих классов.
class Tank():
    def __init__(self, name, speed, damag):
        self.name = name
        self.speed = speed
        self.damag = damag

    def show_Tank(self):
        print(f'Имя {self.name} Скорость: {self.speed} Урон: {self.damag} ')

    def move(self):
        print("Tank " + self.name + " -> Движение")

    def lev_up_1(self):
        self.speed += 20
        print(f'Скорость Танка ИСУ-152 +20 = {self.speed}')

    def lev_up_2(self):
        self.speed += 20
        print(f'Скорость Танка CY-100 +20 = {self.speed}')


tank_1 = Tank('ИСУ-152', 40, 100)
tank_2 = Tank('CY-100', 60, 70)


tank_1.show_Tank()
tank_2.show_Tank()
tank_1.move()
tank_2.move()
tank_2.lev_up_2()
tank_1.lev_up_1()