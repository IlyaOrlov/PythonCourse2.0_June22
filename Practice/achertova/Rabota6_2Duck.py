class Duck:
    color = "grey"

    def __init__(self, n, w):
        self.name = n
        self.weight = w

    @staticmethod
    def voice():
        print(f"Сrack")

    @classmethod
    def duckcolor(cls):
        print(cls.color)

    def whoyouare(self):
        print(f"I`m {self.name}. My weight is {self.weight}")

    def __repr__(self):
        return f"{self.color} Duck {self.name}"

    def __lt__(self, other):
        return self.weight < other.weight

    def who_is_heavier(self, other):
        a = self < other
        if a is True:
            print(f"{other.name}")
        else:
            print(f"{self.name}")

    def __ne__(self, other):
        return self.weight != other.weight

    # def bool(self, b):
    #     return bool(b)
    # ne и bool не совсем поняла, что требуется в задании. Сделала так, что через ne проверяется неравенство,
    # а через bool выводится True(Не равны) или False(Равны)

    def __add__(self, other):
        return self.weight + other.weight


d1 = Duck("Gena", 3)
d2 = Duck("Terminator", 7)
Duck.duckcolor()
Duck.who_is_heavier(d2, d1)
print(f"Вес уток отличается: {d1 != d2}")
print(f"Общий вес уток: {d1 + d2} кг")


