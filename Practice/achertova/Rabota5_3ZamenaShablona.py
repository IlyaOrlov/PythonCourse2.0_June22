s = "Вчера я посетил Макдональдс. Пил там Колу и ел МакЧикен"
impotozameschenie = {"Макдональдс.": "Вкусно и точка.", "Колу": "Черноголовку", "МакЧикен": "Наггетсы"}
for k, v in impotozameschenie.items():
    s = s.replace(k, v)
print(s)


