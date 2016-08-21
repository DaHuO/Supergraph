
def generate_all(n, obj, j):
    for x in range(j):
        res = []
        gen_tmp = next(obj)
        len_of_zero = n - len(gen_tmp)*2 - 2
        num = ''
        num += gen_tmp + '1'
        for i in range(len_of_zero):
            num += '0'
        num += gen_tmp + '1'
        res.append(num)
        for y in range(2, 11):
            factor =str(y ** (n-len(gen_tmp)-1) + 1) 
            res.append(factor)
        print ' '.join(a for a in res)

def generate():
    i = 0
    while 1:
        i += 1
        yield str(bin(i))[2:]

t = int(raw_input())
for i in range(t):
    n, j = [int(x) for x in raw_input().split(' ')]
    obj = generate()
    print 'Case #%d:'%(i+1)
    generate_all(n, obj, j)
