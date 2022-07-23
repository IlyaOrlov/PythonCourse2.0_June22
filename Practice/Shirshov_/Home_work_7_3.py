# Реализовать систему, эмулирующую работу с банкоматами.
# Создать семейство классов банкоматов, хранящих определенные суммы и поддерживающих различные
# операции (одни банкоматы принимают и выдают наличные, другие позволяют еще и проводить онлайн платежи).
# Операции реализуются посредством методов, выводящих название операции и меняющих (при необходимости)
# количество наличных в банкомате.
# Для тестирования системы необходимо реализовать алгоритм, обходящий список банкоматов разного типа и
# запрашивающий у каждого банкомата информацию о количестве наличных и наборе поддерживаемых операций.*

class Bankomat:
    def __init__(self, name, cash, online):
        self.bank_name = name
        self._sum_cash = cash
        self._online = online

    @property
    def sum_cash(self):
        return self._sum_cash

    @sum_cash.setter
    def sum_cash(self, cash):
        if self._sum_cash + cash < 0:
            print('Данной суммы нет в банкомате, обратитесь, пожалуйста, в друой банкомат')
        else:
            self._sum_cash += cash

    @property
    def online_o(self):
        if self._online is True:
            return f'Операция перевода онлайн возможна'
        else:
             return f'Операция перевода онлайн данному теминалу не доступна'

    def __repr__(self):
        return (f' Информация о банкомате: \n Принадлежность: {self.bank_name}\n '
                f'Сумма на счете: {self._sum_cash}\n Операции: {self.online_o}')


class NewBank(Bankomat):
    def __init__(self, name, cash, online, country):
        super().__init__(name, cash, online)
        self.n_country = country

    def __repr__(self):
        return super().__repr__() + f'\n Код оператора: {self.n_country}'

    def online_o_new(self):
        if self.n_country != 'RU' and self._online is True:
            return super().online_o + ' и доступна операция перевода заграницу'
        else:
            return super().online_o + ', но операция перевода заграницу пока не доступна!'


b1 = Bankomat('Alfa', 3000, True)
b1_2 = Bankomat('KFC', 700, False)
b2 = NewBank('Ros', 5000, True, 'RU')
b2_2 = NewBank('Sber', 10000, False, 'DE')
b2_3 = NewBank('Potato', 3000, True, 'BY')
b2_4 = NewBank('Cuba', 100, True, 'USA')


lstb = [b1, b1_2, b2, b2_2, b2_3, b2_4]

for i in lstb:
    try:
        #print(i)
        print(f'{i.bank_name} - {i.sum_cash}')
        print(f'{i.bank_name} - {i.online_o_new()}')
    except AttributeError:
        print(f'{i.bank_name} - {i.online_o}')
