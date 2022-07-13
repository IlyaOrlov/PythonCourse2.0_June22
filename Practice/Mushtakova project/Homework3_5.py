s1 = input("Введите слово палиндром: ")
s2 = s1.istitle([::-1])
c = s1 == s2
print(c)
