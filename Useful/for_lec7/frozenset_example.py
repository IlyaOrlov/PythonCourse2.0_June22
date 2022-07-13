s1 = {"Ivanov", "Petrov", "Sidorov"}
s2 = {"Tapkin", "Lozhkin", "Ivanov", frozenset(s1)}
print(s2)

lst = [1, 2, 5, 2]
lst = list(frozenset(lst))
print(lst)
