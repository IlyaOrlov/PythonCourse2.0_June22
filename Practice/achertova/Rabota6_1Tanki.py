class LandingTank:
    protection = "armor"
    weight = "heavy"
    use = "land"
    maxspeed = 60

    def __repr__(self):
        return f"{self.protection} {self.weight} tank for {self.use}"

    @staticmethod
    def moveright():
        print(f"=>")

    @staticmethod
    def moveleft():
        print(f"<=")

    @staticmethod
    def averagespeed(s, t):
        v = s / t
        return v


class Amphibian:
    weight = "light"
    swimby = "sidefloat"
    maxspeed = 44

    def swim(self):
        print("Bul`k")

    def shoot(self):
        print(f"***")

MarkIX = LandingTank()
AAV7 = LandingTank()
T38 = Amphibian()
T33 = Amphibian()

T33.swim()
AAV7.moveleft()
T38.shoot()