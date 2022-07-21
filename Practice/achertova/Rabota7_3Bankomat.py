class CashMachine:

	def __init__(self, s):
		self.sumin = s

	def __repr__(self):
		return f"Сумма в банкомате {self.sumin}. Поддерживаются операции пополнения и списания счета."

	def accept_cash(self, ac):
		self.sumin += ac
		print(f"Ваш счет пополнен на {ac} рублей. Баланс: {self.sumin}")

	def give_out_cash(self, goc):
		self.sumin -= goc
		print(f"С вашего счета списано {goc} рублей. Баланс: {self.sumin}")


class CashMachineOnline(CashMachine):

	def __repr__(self):
		return f"Сумма в банкомате {self.sumin}. Поддерживаются операции пополнения, списания со счета, " \
		       f"перевод средств онлайн. "

	def give_out_cash_online(self, goc):
		CashMachine.give_out_cash(self, goc)
		print(f"Онлайн-операция")


cm1 = CashMachine(1000)
cm2 = CashMachine(2000)
cm3 = CashMachineOnline(3000)
cm4 = CashMachineOnline(4000)

tpl = (cm1, cm2, cm3, cm4)
for i in tpl:
	print(i)
