#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

MAX = 100
t = int(input())
for i in range(t):
    digits_found = { x : False for x in range(10) }
    n = int(input())
    j = 1
    while j < MAX:
        num = j * n
        s = str(num)
        for c in s:
            digits_found[int(c)] = True
        if not False in digits_found.values():
            break
        j = j + 1
    if j == MAX:
        output = "INSOMNIA"
    else:
        output = str(num)
    print("Case #{}: {}".format(i + 1, output))
