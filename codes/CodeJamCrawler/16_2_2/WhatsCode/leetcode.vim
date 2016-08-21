T = int(raw_input())
for i in xrange(T):
    inp = raw_input().split()
    C = inp[0]
    J = inp[1]
    ans1, ans2 = [], []

    def get(i, c, inputs, aa):
        if i == len(inputs):
            aa.append(int(c))
            return
        if inputs[i].isdigit():
            c += inputs[i]
            get(i+1, c, inputs, aa)
        else:
            for j in xrange(0, 10):
                k = c
                k += str(j)
                get(i+1, k, inputs, aa)

    get(0, '', C, ans1)
    get(0, '', J, ans2)
    anslen = 9999999999999999999
    aj, ac = 0, 0
    for j in xrange(len(ans2)-1, -1, -1):
        for c in xrange(len(ans1)-1, -1, -1):
            k = abs(int(ans1[c]) - int(ans2[j]))
            if k <= anslen:
                anslen = k
                aj = j
                ac = c
    # print ans1, ans2, ac, aj
    acc = str(ans1[ac])
    ajj = str(ans2[aj])
    while len(acc) < len(J):
        acc = '0' + acc
    while len(ajj) < len(J):
        ajj = '0' + ajj
    print "Case #" + str(i+1)+ ": " + acc + " " + ajj
