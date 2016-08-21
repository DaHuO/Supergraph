__author__ = 'sushrutrathi'


with open('input.txt') as f:
    t = int(f.readline().split()[0])
    for k in range(1,t+1):
        st = f.readline().replace('\n','')
        ans = 0
        for i in range(1,len(st)):
            if st[i] != st[i-1]:
                ans += 1


        if st[len(st)-1]=='-':
            ans += 1

        print('Case #' + str(k) + ': ' + str(ans))
