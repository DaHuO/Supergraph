import re
def check(pancakes):
    if '+' not in pancakes:
        return 1
    else:
        type = pancakes[0] == '-'

        string = re.findall('[-]+', pancakes)
        if type:
            return 1 + (len(string)-1)*2
        else:
            return len(string)*2

        return 0

T = int(input())
f = open('workfile', 'w')
for j in range(1, T + 1):
    pancakes = raw_input()
    print(check(pancakes))
    f.write("Case #%s: %s\n" % (j, check(pancakes)))