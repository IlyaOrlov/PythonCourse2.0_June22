# 1.Спроектировать классы (один или несколько) для игры в танки и создать экземпляры этих классов.
class Tank():
    def __int__(self, name, speed, damag):
        self.name = name
        self.speed = speed
        self.damag = damag

    def show_Tank(self):
        dis = (self.name + "Имя" + self.speed + "Скорость" + self.damag + "Урон").title()
        print(dis)

    def lev_up(self):
        self.speed += 1

    def move(self):
        print("Tank " + self.name + "Движение")


tank_1 = Tank('ИСУ-152', 10, 10) # Почему -то не создается объект tank_1
tank_2 = Tank("CY-100, 5, 5")

tank_1.show_Tank()
tank_2.lev_up()
tank_1.move()
tank_2.move()