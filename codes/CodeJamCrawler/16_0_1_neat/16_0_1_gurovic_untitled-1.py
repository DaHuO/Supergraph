import sys
sys.stdin = open("a.in")
sys.stdout = open("a.out", "w")
T = int(input())
for i in range(T):
    n = int(input())
    if n == 0:
        print('Case #' + str(i + 1) + ": " + 'INSOMNIA')
    else:
        nn = n
        s = set(list(str(nn)))
        while len(s) < 10:
            nn += n
            s |= set(list(str(nn)))
        print("Case #" + str(i + 1) + ": " + str(nn))
