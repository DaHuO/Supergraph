T = int(raw_input())
for t in range(1, T+1):
    N = int(raw_input())
    if N == 0:
        print ("Case #%d: INSOMNIA") % t
    else:
        ans = 0
        dict = {}
        while len(dict) < 10:
            ans = ans + N
            tmp = ans
            while tmp > 0:
                d = tmp % 10
                tmp = tmp / 10
                if dict.has_key(d):
                    dict[d] = dict[d] + 1
                else:
                    dict[d] = 1
        print ("Case #%d: %d") % (t, ans)

