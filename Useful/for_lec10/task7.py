import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', line, re.M|re.I)
if matchObj:
    print(f"match --> matchObj.group(): {matchObj.group()}")
else:
    print("No match!")

searchObj = re.search(r'dogs', line, re.M|re.I)
if searchObj:
    print(f"search --> searchObj.group(): {searchObj.group()}")
else:
    print("Nothing found!")
