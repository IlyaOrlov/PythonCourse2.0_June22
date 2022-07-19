import re

# line = 'netops.microsoft.com - - [01/Jul/1995:07:43:07 -0400] "GET /history/gemini/gemini.html HTTP/1.0" 200 2522'
# res = re.findall(r'(.*) - - \[(.*) -0400\] "GET.*$', line, re.M|re.I)
# print(res)

res = []
with open('log.txt', 'r') as f:
    for line in f:
        res += re.findall(r'(.*) - - \[(.*) -0400\] "GET.*$', line, re.M | re.I)

print(res)