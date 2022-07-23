class MyIter:
	def __init__(self, str):
		self.j = 0
		self.i = 0
		self.str = str

	def __iter__(self):
		return self

	def __next__(self):
		if self.i < len(str):
			while str[self.i] != "/":
				self.i += 1
			else:
				a = str[self.j:self.i]
				self.j = self.i
				self.i += 1
				return a
		else:
			raise StopIteration


str = "Python /стал /одним из самых /популярных языков/"
mi = MyIter(str)
it = iter(mi)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# str = "Python /стал /одним из самых /популярных языков/"
# j = 0
# for i in range(len(str)):
# 	if str[i] == "/":
# 		print(str[j:i])
# 		j = i


