import sys
import math

sys.stdin = open ('input.txt', 'r')
sys.stdout = open ('output.txt', 'w')


T = int (sys.stdin.readline())

for t in range (1, T + 1) :
    n = int (sys.stdin.readline ())
    cnt = [0] * 10

    if n == 0 :
        print ('Case #' + str (t) + ': INSOMNIA')
        continue

    need = 10

    ans = n

    for i in range (1, 1000000) :
        v = n * i
        while v > 0 :
            vv = v % 10
            if cnt[vv] == 0 :
                need -= 1
                cnt[vv] = 1
            v //= 10
        if need == 0 :
            ans = n * i
            break
    print ('Case #' + str (t) + ': ' + str (ans))