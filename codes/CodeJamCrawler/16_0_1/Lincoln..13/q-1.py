f = open('C:\Users\LINCOLN\Desktop\wow.txt', 'w')
f.truncate()
p = open('C:\Users\LINCOLN\Desktop\A-large.in', 'r+')
w = p.read()
w = w.split('\n')
for _ in range(int(w[0])):
    n = int(w[_+1])
    a = [0,1,2,3,4,5,6,7,8,9]
    b = []
    if n == 0:
        z = "Case #{}: {}".format(_+1, "INSOMNIA")
        f.write(z)
        f.write('\n')
    else:
        i = 1
        while a != b:
            k = i*n
            i+=1
            c = map(int,str(k))
            for l in c:
                if l not in b:
                    b.append(l)
            b = sorted(b)
        z = "Case #{}: {}".format(_+1, k)
        f.write(z)
        f.write('\n')
f.close()
p.close()