def rb(a, b):
    c = 0
    d = 1
    while a != 0:
        c += (a%2)*d
        a //= 2
        d *= b
    return c

def prime(x):
    y = int(x**0.5+0.5)
    for i in range(2, y+1):
        if (x%i) == 0:
            return i
    return 0

t = raw_input()
l = map(int, raw_input().split())
print "Case #1:"
a = l[0]
b = l[1]
c = 2**(a-1)+1
limit = 2**a
cnt = 0
while c < limit and cnt < b:
    flag = True
    l = []
    for i in range(2, 10+1):
        z = prime(rb(c, i))
        if z == 0:
            flag = False
            break
        l.append(z)
    if flag:
        print format(c, 'b'), ' '.join(map(str, l))
        cnt += 1
    c += 2
