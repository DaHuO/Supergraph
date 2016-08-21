T = raw_input()
T = int(T)
lst = []

for i in range(0, T):
    N = raw_input()
    lst.append(N)

i = 1
for n in lst:
    lst = list()
    lst_happy = list()
    lst_sad = list()
    s_happy = str()
    s_sad = str()
    flip = 0
    for s in n:
        lst_happy.append("+")
        lst.append(s)
        lst_sad.append("-")
        s_happy = s_happy + "+"
        s_sad = s_sad + "-"

    if(n == s_happy):
        print "Case #%d: %d" % (i,0)
        i = i+1
        continue
    if(n == s_sad):
        print "Case #%d: %d" % (i,1)
        i = i+1
        continue

    while(lst != lst_happy):
        it = 1
        opposite = "+"
        while(lst[0] == lst[it]):
            it = it + 1

        opposite = lst[it]

        for ls in range(it):

            lst[ls] = opposite
        if (lst == lst_sad):
            lst = lst_happy
            it = it + 1
            flip = flip + 1
        flip = flip + 1
    print "Case #%d: %d" % (i,flip)
    i = i + 1