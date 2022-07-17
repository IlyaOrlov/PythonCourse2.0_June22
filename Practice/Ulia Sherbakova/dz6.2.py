class Duck:
    color = "red"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"утка {self.name} вес {self.weight}"

    def __lt__(self, other):
        v = self.weight < other.weight
        if v == True:
            return other.name
        else:
            return self.name

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        return self.weight + other.weight

    @staticmethod
    def say():
        print("Сrack")

    @classmethod
    def what_color(cls):
        print(cls.color)

e1 = Duck("Малышка", 3)
e2 = Duck("Крупняшка", 9)
print(f"Вес уток равен {e1 + e2}")
print(f"Тяжелее утка {e2 < e1}")
print(f"Тяжелее утка {e1 < e2}")
print(f"Тяжелее утка {e2 > e1}")
print(f"Тяжелее утка {e1 > e2}")
print(f"Вес разный? {e1 != e2}")
print(e1)
print(e2)
Duck.what_color()
e1.say()