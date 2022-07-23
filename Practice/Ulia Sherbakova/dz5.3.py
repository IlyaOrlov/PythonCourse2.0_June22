s = 'строкадлязаменысимволов'
x = {'а': 3, 'з': 5, 'о': 7}

for key in x.keys():
    s = s.replace(key, str(x[key]))

print(s)