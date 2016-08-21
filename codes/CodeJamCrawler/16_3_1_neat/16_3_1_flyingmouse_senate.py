def gen_alpha():
    a = []
    for i in xrange(26):
        a.append(chr(65+i))
    return a

alpha = gen_alpha()

def evacuate(a):
    res = ""
    while sum(a) > 0:
        m = max(a)
        liste = [i for i, j in enumerate(a) if j == m]
        size = len(liste)
        if m == 1:
            if size % 2 == 1:
                res += " " + alpha[liste[0]]
                a[liste[0]] -= 1
            else:
                res += " " + alpha[liste[0]] + alpha[liste[1]]
                a[liste[0]] -= 1
                a[liste[1]] -= 1
        else:
            if size == 1:
                index = liste[0]
                if sum(a) != 3:
                    res += " " + alpha[index] * 2
                    a[index] -= 2
                else:
                    res += " " + alpha[index] * 1
                    a[index] -= 1
            else:
                index1, index2 = liste[0], liste[1]
                res += " " + alpha[index1] + alpha[index2]
                a[index1] -= 1
                a[index2] -= 1
    return res

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    N = raw_input()
    a = map(int, raw_input().split(" "))
    #print a
    print "Case #{}:{}".format(i, evacuate(a))
