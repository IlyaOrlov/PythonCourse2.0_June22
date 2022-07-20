class LandingTank:
    protection = "armor"
    weight = "heavy"
    use = "land"
    maxspeed = 60

    def __repr__(self):
        return f"{self.protection} {self.weight} tank for {self.use}"

    @staticmethod
    def move_right():
        print(f"=>")

    @staticmethod
    def move_left():
        print(f"<=")

    @staticmethod
    def average_speed(s, t):
        v = s / t
        return v


class Amphibian:
    weight = "light"
    swimby = "sidefloat"
    maxspeed = 44

    @staticmethod
    def swim():
        print("Bul`k")

    @staticmethod
    def shoot():
        print(f"***")


MarkIX = LandingTank()
AAV7 = LandingTank()
T38 = Amphibian()
T33 = Amphibian()

T33.swim()
AAV7.move_left()
T38.shoot()
MarkIX.s = 100
MarkIX.t = 2
v = MarkIX.average_speed(MarkIX.s, MarkIX.t)
print(f"Сегодня средняя скорость MarkXI составила {v} км/ч")