import re

i = int(input())
for case in range(i):
    woord = ""
    for letter in str(input()):
        woord = max(letter + "" + woord, woord + "" + letter)
    print("Case #{}: {}".format(case + 1,woord))
