def last_word(s):
    s1 = s[0]
    s = s[1:]

    while len(s) > 0:
        c = s[0]
        s = s[1:]
        if s1[0] > c:
            s1 = s1 + c
        else:
            s1 = c + s1
    return s1

f = open("input.txt")
lines = f.readlines()
f.close()
n = int(lines[0])

for i in range(n):
    print "Case #" + str(i+1) + ": " + last_word(lines[i+1].rstrip())

