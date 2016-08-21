import random

N = 32
J = 500

ans = []
dic = {}
while len(ans) < J:
    s = '1' + ''.join([random.choice('01') for i in range(N - 2)]) + '1'
    res = [s]

    for i in range(2, 11):
        t = int(s, i)
        for i in range(2, min(t, 50000)):
            if t % i == 0:
                res.append(i)
                break
        else:
            break

    if len(res) == 10 and res[0] not in dic:
        dic[res[0]] = True
        ans.append(res)
out = open('out.txt', 'w')
print ('Case #1:')
out.write('Case #1:\n')
for item in ans:
    print (' '.join(map(str, item)))
    out.write(' '.join(map(str, item)) + '\n')
