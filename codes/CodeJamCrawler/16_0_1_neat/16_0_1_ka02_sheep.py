t = int(raw_input())
test = t
def sleep(n):
    a = []
    b = []
    i = 1
    c = n
    while len(a) != 10:
        c = n * i
        b = set(map(int, str(c)))
        a = set(list(a) + list(b))
        i += 1
    return str(c)

while t > 0:
    n = int(raw_input())
    if n == 0:
        print "Case #" + str(test - t + 1) + ":" + " " + "INSOMNIA"
    else:
        print "Case #" + str(test - t + 1) + ":" + " " + sleep(n)
    t -= 1