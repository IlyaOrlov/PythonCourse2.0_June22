s = "Вчера я посетил Макдональдс. Пил там Колу и ел МакЧикен"
impotozameschenie = {"Макдональдс.": "Вкусно и точка.", "Колу": "Черноголовку", "МакЧикен": "Наггетсы"}
s2 = s.split(" ")
for i in s2:
    for k, v in impotozameschenie.items():
        if i == k:
            s = s.replace(i, v)
print(s)

#Готово