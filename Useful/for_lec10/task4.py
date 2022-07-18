import json


my_list = ['foo', {'bar': ('baz', None, 1.0, 2)}]
with open('my_file.txt', 'w') as f:
    my_list = json.dumps(my_list)
    f.write(my_list)
