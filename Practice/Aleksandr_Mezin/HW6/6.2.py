class Duck:
    clr = "gray"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __add__(self, other):
        return d1.weight + d2.weight

    def __repr__(self):
        return f"{self.name} {self.weight}"

    def __lt__(self, other):
        if d1.weight < d2.weight:
            return d2.name
        else:
            return d1.name

    def __ne__(self, other):      # непонятно как реализовать
        if d1.weight != d2.weight:
            print("bool")

    @staticmethod
    def crack():
        print("Crack")

    @classmethod
    def color(cls):
        print(cls.clr)


d1 = Duck("Donald", 1.75)
d2 = Duck("McDuck", 2.00)
print(d1)
d1.crack(), d1.color()
print(d2)
d2.crack(), d2.color()
print(f"{d1 < d2} тяжелее")
print(f"Общий вес: {d1 + d2}")
print(d1.weight != d2.weight)
