T = int(raw_input())

for case in range(T):
    line = raw_input().strip()[::-1]

    count = 0
    current = '+'
    flip = {
        '-': '+',
        '+': '-'
    }

    for char in line:
        if char != current:
            count += 1
            current = flip[current]

    print "Case #{}: {}".format(case + 1, count)
