# Спроектировать классы (один или несколько) для игры в танки и создать экземпляры этих классов.


class Tank:
    color = "grey"
    power = 2000
    speed = 50

    def __init__(self, name, country, years):
        self.tank_name = name
        self.tank_country = country
        self.tank_years = years

    @staticmethod
    def show():
        return print(f'название - {i.tank_name} , мощность: {i.power}, скорость : {i.speed}')

    @staticmethod
    def bah():
        return print("бах-бах-бах")


class NewTank(Tank):
    def __init__(self, name, country, years):
        super().__init__(name, country, years)
        self.power = self.power * 2
        self.speed = self.speed * 3

    @staticmethod
    def bah():
        print("бам!!! бам!!!")


t1_T34 = Tank('T34', 'RU', '1943')
t_new = NewTank('new_T34', 'RU', '2000')
t2_Tiger = Tank('Tiger', 'RU', '1992')

lst = [t1_T34, t_new, t2_Tiger]


for i in lst:
    information = i.show()
    babah = i.bah()
