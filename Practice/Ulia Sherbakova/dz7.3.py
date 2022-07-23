class Bankomat:
    name = "Центробанк"
    nalichka = 100000000

    @classmethod
    def get_name(cls):
        print(f'Название банкомата: {cls.name}')

    def __init__(self, symma_na_schete):
        self.symma_na_schete = symma_na_schete

    def __repr__(self):
        return f"Количеcтво наличных в банке: {self.nalichka} Банкомат принимает и выдает наличные"

    def nalich_vidacha(self, vidacha):
        if vidacha > self.symma_na_schete:
            print("На вашем счете недостаточно средств")
        else:
            print(f"Получите {vidacha} руб. На вашем счете: {self.symma_na_schete - vidacha} руб. Наличных в банке осталось: {self.nalichka - vidacha} руб")

    def nalich_priem(self, priem):
        print(f"Забрал {priem} руб. На вашем счете: {self.symma_na_schete + priem} руб.")


class SberBankomat(Bankomat):
    name = "Сбербанк"
    nalichka = 100000


class TinkoffBankomat(Bankomat):
    name = "Тинькофф"
    nalichka = 5000000

    def __repr__(self):
        return f"Количеcтво наличных в банке: {self.nalichka} Банкомат принимает и выдает наличные. Доступны онлайн платежи"


    def online_plategi(self, perevod):
        print(f"Перевод {perevod} выполнен. На вашем счете: {self.symma_na_schete - perevod} руб.")



b1 = Bankomat(10000)
b2 = SberBankomat(5000)
b3 = TinkoffBankomat(80000)
Bankomat.get_name()
b1.nalich_priem(1000)
SberBankomat.get_name()
b2.nalich_vidacha(2000)
TinkoffBankomat.get_name()
b3.online_plategi(9000)

lst = [b1, b2, b3]
for b in lst:
    print(b)



