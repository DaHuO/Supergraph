T = int(input())

for i in range(T):
    s = raw_input()

    count = 0
    old = '+'
    for c in s[::-1]:
        if c == old:
            continue
        else:
            old = c
            count += 1
    print("Case #%d: %d" % (i+1, count))
