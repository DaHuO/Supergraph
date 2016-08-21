file = open('C:\\Users\\V\\Downloads\\A-large.in','r')
f = file.read()
res = f.split("\n")
print res
T = int(res[0])
print T
file.close()
file = open('C:\\Users\\V\\Downloads\\Google1.out','w')
for i in range(0, T):
    a = int(res[i + 1])
    if a != 0:
        b = []
        o = a
        while len(b) < 10:
            c = a
            p = 0
            while c >= 1 and p < 10:
                d = c % 10
                if d not in b:
                    b.append(d)
                p = p + 1
                c = c / 10
            k = a    
            a = o + a
        print "Case #" + str(i+1) + ": " + str(k)
        file.write("Case #" + str(i+1) + ": " + str(k) + "\n")
    else:
        print "Case #" + str(i+1) + ": " + "INSOMNIA"
        file.write("Case #" + str(i+1) + ": " + "INSOMNIA" + "\n")
file.close()        