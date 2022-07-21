import re

res = []
patt = re.compile("ERROR-\d+")
with open('log_file.txt', 'r') as f:
    for line in f:
        res += re.findall(patt, line)

print(res)

res_attr = []
lst_attrs = ['_a', 'b', '__c', '_d']  # _protected
for attr in lst_attrs:
    res_attr += re.findall('^_\w$', attr)

print(res_attr)
