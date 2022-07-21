m = [[1, 2, 3],
     [5, 5, 6],
     [7, 8, 9]]
a = 5
index1 = 0
index2 = 0
while index2 < len(m[0]):
    stolbik = [row[index2] for row in m]
    if a in stolbik:
        index1 = 0
        while index1 < len(m):
            del m[index1][index2]
            index1 += 1
    else:
        index2 += 1
print(m)