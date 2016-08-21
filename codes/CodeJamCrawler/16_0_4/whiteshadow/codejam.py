__author__ = 'sushrutrathi'


with open('input.txt') as f:
    t = int(f.readline().split()[0])
    for case in range(1,t+1):
        k , c , s = [int(x) for x in f.readline().split()]
        ans = []
        for g_index in range(1,k+1):
            pos = g_index
            for iter in range(2,c+1):
                pos = (pos-1)*k + 1
            ans.append(pos)


        print('Case #' + str(case) + ': ', end='')
        for i in ans:
            print(str(i) + ' ',end='')
        print('\n')
