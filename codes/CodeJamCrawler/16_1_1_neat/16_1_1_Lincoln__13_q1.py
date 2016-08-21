f = open('C:\Users\LINCOLN\Desktop\wow1.txt', 'w')
f.truncate()
poda = open('C:\Users\LINCOLN\Desktop\A-small-attempt0.in', 'r+')
w = poda.read()
w = w.split('\n')
for _ in range(int(w[0])):
    n = w[_+1]
    x1 = []
    k = len(n)
    i = 0
    def add_1(x,val):
        return val+x
    def add_2(x,val):
        return x+val
    while i<k:
        if i == 0:
            x1 = list(n[i])
        elif i == 1:
            a = n[i] + x1[0]
            b = x1[0] + n[i]
            x1 = []
            x1.append(a)
            x1.append(b)
        else:
            x2 = []
            for j in x1:
                a = add_1(j,n[i])
                b = add_2(j,n[i])
                x2.append(a)
                x2.append(b)
                
            x1 = []
            x1 = x2
        i += 1
    x1.sort()
    z = "Case #{}: {}".format(_+1, x1[len(x1)-1])
    f.write(z)
    f.write('\n')
f.close()
poda.close()