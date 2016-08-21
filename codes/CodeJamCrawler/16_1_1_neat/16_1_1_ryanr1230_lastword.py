T = int(raw_input())
for i in range(T):
    line = raw_input()
    new_line = ''
    for c in line:
        if len(new_line) == 0:
            new_line += c
        else:
            if new_line[0] > c:
                new_line += c
            else:
                new_line = c + new_line
    print "Case #%d:" % (i + 1), new_line
