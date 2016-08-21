d = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J" ,"K" ,"L" ,"M" ,"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def arrange(n, l, a):
    a1 = []
    l1 = []
    for i in range(n):
        k = l.index(max(l))
        a1.append(a[k])
        l1.append(l[k])
        l[k] = 0
    return l1, a1

def f(n, l1, a):
    if sum(l1)==0:
        return "done"
    if sum(l1)%2==0:
        l1[0]-=1
        l1[1]-=1
        return d[a[0]]+d[a[1]], l1, a
    else:
        l1[0]-=1
        return d[a[0]], l1, a


t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    l = map(lambda x: int(x), raw_input().split(" "))
    s = ""
    T = True
    a = range(n)
    while T:
        l1 = arrange(n, l, a)
        s1 = f(n, l1[0], l1[1])
        if type(s1) == str:
            break
        s = s + s1[0] + " "
        l = s1[1]
        a = s1[2]
    print "Case #{}: {}".format(i+1, s)
