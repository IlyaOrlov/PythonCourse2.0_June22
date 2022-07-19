import json

with open('my_file.txt', 'r') as f:
    res = f.read()

print(res)
print(type(res))

res = json.loads(res)
print(res)
print(type(res))
res.append('attr')
print(res)