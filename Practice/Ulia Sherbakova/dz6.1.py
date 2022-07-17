class GreenTank:
    model = "Т34"

    def __init__(self, speed, power):
        self.speed = speed
        self.power = power

    def show_tank(self):
        print(f"Модель танка: {self.model}, его мощность {self.power}, его скорость {self.speed}")

class BlackTank(GreenTank):
    model = "Армата"


e1 = GreenTank(50, 20)
e2 = BlackTank(70, 10)

e1.show_tank()
e2.show_tank()
