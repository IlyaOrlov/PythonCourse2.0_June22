from itertools import *

# Функция 1

data = list(combinations('password',4))
for item in data:
    print(item)

# Функция 2

it1 = [1, 2, 3]
it2 = [4, 5]
it3 = [6, 7]
lists_in_list = [it1, it2, it3]
rez = chain.from_iterable(lists_in_list)
print(list(rez))


# Функция 3

def greater_than_five(str):
    return len(str) != 5

data = list(
    filterfalse(
        greater_than_five,
        ['hello', 'i', 'write', 'cool', 'code']
    )
)
print(data)