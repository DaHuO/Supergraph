T = raw_input()
T = int(T)
lst = []

for i in range(0, T):
    N = raw_input()
    lst.append(N)

S = []
count = 1
for n in lst:
    for i in str(n):
        if len(str(n)) == 1:
            string = i
            continue
        if len(S) == 0:
            S.append(i)
            continue
        if i < (S[0]):
            S.append(i)
        else:
            S = list(i) + S
        string = str()
        for s in S:
            string = string + str(s)
    print "Case #%d: %s" % (count,string)
    count = count + 1
    S = []
count = 0