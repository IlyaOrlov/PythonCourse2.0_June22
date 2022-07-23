i = 0
spisok = ['Ты сам то понял, что написал?', 'Аргументируй', 'И?']
while True:
    print("Введи слово:")
    word = input()

    if word.upper() == "ХВАТИТ":
        print("как скажешь!")
        break
    if i > len(spisok) - 1:
        i = 0
    print(spisok[i])
    i += 1