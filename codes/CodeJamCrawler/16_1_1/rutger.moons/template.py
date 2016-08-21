__author__ = 'rutger'

problemName = "problem.txt"
f = open(problemName, 'w')

T = int(input())
for t in range(T):
    pass
    # do input
    s = input()

    # solve input
    current = s[0]
    for i in range(1, len(s)):
        letter = s[i]
        if letter >= current[0]:
            current = letter + current
        else:
            current = current + letter


    # print result
    f.write("Case #%d: %s\n" % (t+1, current))



f.close()