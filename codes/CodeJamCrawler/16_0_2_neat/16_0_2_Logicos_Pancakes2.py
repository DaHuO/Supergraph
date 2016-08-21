import re

i = int(input())
for case in range(i):
    stack = str(input())
    stack = re.sub("--*","-",stack)
    stack = re.sub("\+\+*","+",stack)
    if stack[-1] == "-":
        stack = stack + "+"
    aantal = len(stack) - 1

    print("Case #{}: {}".format(case + 1,aantal))
