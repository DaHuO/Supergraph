__author__ = 'sushrutrathi'


with open('input.txt') as f:
    t = int(f.readline().split()[0])
    for k in range(1,t+1):
        n = int(f.readline().split()[0])
        if n == 0 :
            ans = 'INSOMNIA'
        else:
            i = 1
            sts = set([])
            while True:
                m = n * i
                st = str(m)
                ans = st
                tmp = set(st)
                sts = sts.union(tmp)
                if len(sts) == 10:
                    break
                i += 1
                if i > 1000:
                    ans = 'INSOMNIA'
                    break



        print('Case #' + str(k) + ': ' + ans)
