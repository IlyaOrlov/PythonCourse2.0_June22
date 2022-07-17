m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
a = 9
index1 = 0
index2 = 0
while index2 < 3:
      stolbik = [row[index2] for row in m]
      if a in stolbik:
            while index1 < 3:
                  del m[index1][index2]
                  index1 += 1
            break
      index2 += 1
print(m)
# Готово