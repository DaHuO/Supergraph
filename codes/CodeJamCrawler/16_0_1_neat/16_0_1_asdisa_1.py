inp = open('/home/denisthepirate/py/Input1')
data = []
k = inp.read().split('\n')
del k[len(k)-1]
for i in k:
    data.append(int(i))
inp.close()
for i in range(1, int(data[0])):
    n = int(data[i])
    s = set()
    if n == 0:
        print('Case #' + str(i) + ':', 'INSOMNIA')
    else:
        c = 1
        while(len(s) < 10):
            for j in str(c*n):
                s.add(j)
            c += 1
        print('Case #' + str(i) + ':', str((c-1)*n))
