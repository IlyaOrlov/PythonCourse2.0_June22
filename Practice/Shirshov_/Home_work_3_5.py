# Программа проверяющая, что слова, введённое пользователем, является палиндромом.
# Программа выводит True или False


print("Программа проверяет, что введённые слова является палиндромом.")


flag_start = True


while flag_start:
    st1 = input("Введите слово, которое является плиндром: ")
    if st1.isalpha() == True and st1.isspace() == False:
        st2 = st1.lower()
        res = (st2 == st2[::-1])
        if res:
            print(res)
            print(f"Строка являестя палиндромом {st1} полиндром {st1[::-1]}")
            flag_start = False
        else:
            print(res)
            print('Строка не является полиндромом попробуйте еще раз')
            flag_start = True
    else:
        print("Строка должна состоять из букв (пробелы тоже не допустимы)")
        flag_start = True
