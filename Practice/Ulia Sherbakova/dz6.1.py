class GreenTank:
    model = "Т34"

    def __init__(self, speed, power):
        self.speed = speed
        self.power = power

class BlackTank(GreenTank):
    model = "Армата"


e1 = GreenTank(50, 20)
e2 = BlackTank(70, 10)

print(f"Модель 1 танка: {e1.model}, его мощность {e1.power}, его скорость {e1.speed}")
print(f"Модель 2 танка: {e2.model}, его мощность {e2.power}, его скорость {e2.speed}")
