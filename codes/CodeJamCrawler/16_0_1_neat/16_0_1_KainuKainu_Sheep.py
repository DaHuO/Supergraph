T = int(input())
C = 1
while (C<=T):
    print("Case #%d: " % C,end="")
    N = int(input())
    if N == 0:
        print("INSOMNIA")
        C += 1
    else:
        d = [0]*10
        count = 0
        i = 1
        while (count<10):
            flag = False
            tmp = N*i
            while (tmp>0):
                n = tmp%10
                if not d[n]:
                    d[n] = 1
                    count += 1
                    if count == 10:
                        print(N*i)
                        flag = True
                        break
                tmp = int(tmp/10)
            if flag:
                break
            i += 1
        C += 1

