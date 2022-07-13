class Dog:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    @staticmethod
    def woof():
        print("Woof - woof!")


d1 = Dog("rexx", 'sheepdog')
d2 = Dog("busya", 'sheepdog')
d1.woof()

print(d1.name)
print(d1.__dict__)
print(d1.species)
print(d2.name)
print(Dog.__dict__)
