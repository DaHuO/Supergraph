j = 500
N = 32
aa = [0 for i in range(N)]
dd = [0 for i in range(10)]
dic = {}

def solve(i):
    global j
    global N
    global aa
    global dd
    global dic
    if j <= 0 or i > N-1:
        return
    for it in range(10):
        dd[it] = 0
    for b in range(2,11):
        pf = True
        bn = 0;
        for it in range(N):
            bn = aa[it] + bn * b;
        if b == 10:
            if bn in dic:
                return
        for it in range(2, 10001):
            if bn % it == 0:
                dd[b - 2] = it
                pf = False
                break;
        if pf == True:
            break
        else:
            if b == 10:
                if bn not in dic:
                    dic[bn] = 1;
                    print ("%d" % bn, end = "")
                    for it in range(9):
                        print (" %d" % dd[it], end="")
                    print()
                    j = j - 1
    if i > 14:
        return
    aa[i] = 0
    solve(i + 1)
    aa[i] = 1
    solve(i + 1)
    aa[i] = 0    

def solution():
    global aa
    global N
    aa[0] = 1
    aa[N - 1] = 1
    print ("Case #1:")
    solve(1)
    return 0

if __name__ == '__main__':
    solution()