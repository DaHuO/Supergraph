def dreamAndroids(f, it, check):
    if (f == 0):
        return 'INSOMNIA'
    
    for n in str(it*f):
        check[int(n)] = '1'
    
    if (''.join(check) == '1111111111'):
        return it*f

    else:
        it = it+1;
        return dreamAndroids(f, it, check)

f = open('A-large.in', 'r')
g = open('A-large.out', 'w')
num = int(f.readline())

for i in range(1, num+1):
    g.write('Case #'+str(i)+': ')
    g.write(str(dreamAndroids(int(f.readline()[:-1]), 1, list('0000000000'))))
    g.write('\n')

f.close()
g.close()
