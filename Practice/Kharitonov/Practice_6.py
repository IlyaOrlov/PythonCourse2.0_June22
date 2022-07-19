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