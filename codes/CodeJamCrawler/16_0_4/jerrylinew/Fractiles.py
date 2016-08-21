filename = 'D-small-attempt0.out'
target = open(filename, 'w')

t = int(input())

for i in range(t):
    string = input()
    base = string[0]
    if string[1] != ' ':
        base = base + string[1]
        if string[2] != ' ':
            base = base + string[2]
    base = int(base)

    answer = range(base)
    answer = [str(a + 1) for a in answer]
    stringanswer = ' '.join(answer)
    target.write('Case #%d: %s\n' % (i + 1, stringanswer))
