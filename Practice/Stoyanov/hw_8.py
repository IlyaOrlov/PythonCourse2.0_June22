'''1. Реализовать итератор, который бы "читал" заданный текст по параграфам. Символ параграфа задается отдельно.
'''

with open("hw_1.py", "r", encoding="UTF-8") as f:
    text = f.read().split("\n")
    text = iter(text)


print(next(text))
print(next(text))

'''2. Написать генератор для построчного чтения файла.
'''

def gen_line():
    with open("hw_1.py", "r", encoding="UTF-8") as f:
        for line in f.readlines():
            yield line


x = gen_line()
print(next(x))
print(next(x))
print(next(x))

'''3. Напишите свой менеджер контекста, замеряющий и показывающий время исполнения кода внутри него.
'''

