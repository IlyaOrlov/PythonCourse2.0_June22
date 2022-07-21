class Bankomat:
    color = 'grey'

    def __init__(self, name, cash, online):
        self.bank_name = name
        self._sum_cash = cash  # 100
        self._online_o = online

    @classmethod
    def get_color(cls):
        print(f'color is {cls.color}')

    @property  # b1.sum_cash
    def sum_cash(self):
        return self._sum_cash

    @sum_cash.setter   # -200
    def sum_cash(self, cash):
        if self._sum_cash + cash < 0:
            print('Данной суммы нет в банкомате, обратитесь, пожалуйста, в друой банкомат')
        else:
            self._sum_cash += cash

    @property # getr  b1.online_o
    def online_o(self):
        if self._online_o is True:
            return 'Операция перевода онлайн возможна'
        else:
             return 'Операция перевода онлайн данному теминалу не доступна'

    def __repr__(self):
        return f'Информация о банке: {self.bank_name = } {self._sum_cash=} {self.online_o}'


class NewBankomat(Bankomat):

    def __repr__(self):
        print(super().__repr__())
        return 'NewBankomat'


b1 = NewBankomat('B1', 100, True)
print(b1)

