import time
f = open("input.txt", "r+")
lines = tuple(f)

def flip(a):
    i = 0
    l = len(a)
    first = a[i]
    while a[i] == first:
        if a[i] not in ["-", "+"]:
            print "wtf"
        i += 1
        if i == l:
            return True
    return switch(a[:i][::-1]) + a[i:]

def switch(a):
    b = ""
    for c in a:
        if c == "-":
            b += "+"
        else:
            b += "-"
    return b


def count_flips(a):
    i = 0
    while a != True:
        prev = a
        a = flip(a)
        i += 1
    if prev[0] == "+":
        i -= 1
    return i


print count_flips("+")

with open("output.txt", "w+") as o:
    for i in range(1, len(lines)):
        o.write("Case #%d: %s\n" % (i, str(count_flips(lines[i].strip()))))
