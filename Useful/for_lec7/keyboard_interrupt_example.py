# Запускать через командную строку, иначе прерывание перехватывается PyCharm'ом
stop = False
while not stop:
    try:
        print("a")
    except KeyboardInterrupt:
        stop = True

print("The end")
