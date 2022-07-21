import pickle
from lib_worker import Worker


with open("dumpfile", "rb") as f:
    j1 = pickle.load(f)
    j2 = pickle.load(f)

print(f"j1={j1}")
print(f"j2={j2}")

print(j1.get_salary() + j2.get_salary())
