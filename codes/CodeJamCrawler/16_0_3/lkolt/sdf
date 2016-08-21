import random
import math
f = open("out.txt","w")
with f as out:
    print("Case #1:", file = out)
    cnt = int(0)
    while (cnt < 500):
        ls = list()

        num = int(1)
        for i in range(30):
            num = num * 10 + (random.randint(0, 1) % 2)
        num = num * 10 + 1
        #print(int(num), file = out)
        for j in range(9):
            i = j + 2
            inter = int(0)
            powb = int(1)
            m = num
            while (m > 0):
                inter = inter + powb * (m % 10)
                powb = powb * i
                m //= 10
            f = bool(0)
            r = int(math.sqrt(inter)) - 1
            for w in range(min(r, 1000)):
                q = w + 2
                if (inter % q == 0):
                    ls.append(q)
                    f = 1
                    break
            if (f == 0):
                break
        if (len(ls) == 9):
            print('{}'.format(int(num)), end = ' ', file = out)
            for i in range(len(ls)):
                print(ls[i], end = ' ', file = out)
            print(file = out)
            cnt += 1
        
