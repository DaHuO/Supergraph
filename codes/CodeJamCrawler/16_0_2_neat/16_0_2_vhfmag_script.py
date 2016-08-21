ss = list()
for i in range(int(input())):
    ss.append(str(raw_input()))

for t, s in enumerate(ss):
    last = s[0]
    changes = 0
    for char in s[1:]:
        if (char != last):
            last = char
            changes += 1

    if s[-1] == "-":
        changes += 1

    print('Case #' + str(t+1) + ': ' + str(changes))
