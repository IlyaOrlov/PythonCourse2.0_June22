"""1. Реализовать алгоритм сортировки выбором. Алгоритм состоит из следующих шагов:
1.найти наименьший элемент в массиве
2.поменять местами его и первый элемент в массиве
3.найти следующий наименьший элемент в массиве
4.и поменять местами его и второй элемент массива
5.продолжать это пока весь массив не будет отсортирован
arr = [0,3,24,2,3,7]
// здесь реализованный алгоритм
// на выходе должен получиться список, содержащий [0, 2, 3, 3, 7, 24]"""

def index_min(k, min_):
    index_min_ = k
    index_ = k + 1
    for j in arr[k + 1:]:
        if j <= min_:
            min_ = j
            index_min_ = index_
        index_ += 1
    return index_min_


arr = [0, 3, 24, 2, 3, 7]
x = 0
k = 0
for i in arr:
    min_ = i
    for j in arr[k + 1:]:
        if j <= min_:
            min_ = j
    res = index_min(k, min_)
    arr[x], arr[res] = arr[res], arr[x]
    k += 1
    x += 1
print(arr)

'''2. Написать и вызвать функцию, возвращающую первый повторившийся символ в переданном списке. Например, 
для  списка [2, 3, 4, 5, 3, 2] функция должна вернуть 3.'''

def search(lst):
    set_ = set()
    for i in lst:
        if i in set_:
            print(i)
            break
        set_.add(i)


lst = [2, 3, 4, 5, 3, 2]
search(lst)

'''3. Найти и заменить некие шаблоны в строке: есть строка с определенного вида форматированием, необходимо заменить 
в этой строке все вхождения шаблонов на их значение из словаря.'''

def repl(string, dictionary):
    for k in dictionary.keys():
        string = string.replace(k, dictionary[k])
    return string


dictionary = {"мб": "может быть", "спс": "спасибо", "с др": "с днем рождения", }
# Пример ввода: Поздравляю с др, желаю реже видеть спс и тогда мб все будет хорошо.
string = input("Напишите предложение: ")
a = repl(string, dictionary)
print(a)

'''4. Есть список списков (матрица). Каждый внутренний список – это строка матрицы. Необходимо реализовать функцию, 
которая удаляет столбец, который содержит заданную цифру.'''

def del_(matrix, num):
    for x in matrix:
        while True:
            if num in x:
                i = x.index(num)
                for k in matrix:
                    del k[i]
            else:
                break


matrix = [
    [21, 22, 23, 24, 25],
    [26, 27, 28, 29, 30],
    [31, 32, 33, 33, 35],
    [36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45]
]
for j in matrix:
    print(j)

num = int(input("Чтобы удалить столбец введите цифру которая в нем содержится: "))
del_(matrix, num)

for j in matrix:
    print(j)

'''5. Реализовать функциональность, которая бы “сворачивала” и “разворачивала” символы табуляции в файле. То есть, 
на вход передается файл, необходимо заменить все символы табуляции на четыре пробела, либо же заменить все комбинации из
четырех символов пробела на символ табуляции (в зависимости от опции, указанной пользователем).'''

# with open("test.txt", "w") as f:
#     f.write(("1 0")*10)

def write(new_file):
    with open("test.txt", "w") as f:
        f.write(new_file)
    print("Готово!")


print("tab - заменит (1 пробел) на (4 пробела)")
print("space - заменит (4 пробела) на (1 пробел)")
choice = input("Что выберете? ").lower()

with open("test.txt", "r") as f:
    file = f.read()

while True:
    if choice == "tab":
        new_file = file.replace(" ", " "*4)
        write(new_file)
        break
    elif choice == "space":
        new_file = file.replace(" "*4, " ")
        write(new_file)
        break
    else:
        print("Не понимаю тебя.")
        choice = input("tab или space? ")
        continue
