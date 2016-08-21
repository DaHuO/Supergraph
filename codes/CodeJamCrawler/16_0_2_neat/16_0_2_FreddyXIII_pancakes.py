input = open("input.txt",'r')

T = int(input.readline())

case = 0
for i in range(0,T):
    case = case + 1
    panstack = input.readline()
    panstack = panstack.strip('\n')
    count = 0
    last = panstack[0]
    for char in panstack:
        if (char != last):
            count = count + 1
        last = char
    if (last == '-'):
        count = count + 1
    print "Case #" + str(case) + ": " + str(count)
