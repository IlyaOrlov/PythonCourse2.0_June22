import re

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print(f"matchObj.group(): {matchObj.group()}")
    print(f"matchObj.group(1): {matchObj.group(1)}")
    print(f"matchObj.group(2): {matchObj.group(2)}")
else:
    print("No match!")
