import re

res = []
patt = re.compile("ERROR-\d+")
with open('log_file.txt', 'r') as f:
    for line in f:
        res += re.findall(patt, line)

print(res)