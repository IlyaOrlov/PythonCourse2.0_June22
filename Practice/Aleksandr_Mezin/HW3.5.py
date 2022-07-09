s = input("Введите слово: ")
fs = len(s)
es = ""

for i in range(fs-1,-1,-1):
    es += s[i]

if es == s:
    print("True")
else:
    print("False")