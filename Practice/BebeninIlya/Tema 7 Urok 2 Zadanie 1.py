class Tanks:
    weight = 50000
    color = "yellow"
    power = 1000
    speed = 50

    def __init__(self,y ):
        self.model = y
    def start_driving(self):
        print("Поехали! ")
    def shoot(self):
        print ("Phaw")
t1 = Tanks("t-72")
t2 = Tanks("T-34")
t1.start_driving()
t2.shoot()