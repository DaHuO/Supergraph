f = open('A-large.in', 'r')
o = open('output', 'w')
T = f.readline()
F = f.readlines()
for i in range(int(T)):
    o.write("Case #")
    o.write(str(i+1))
    o.write(": ")
    test = '0123456789'
    N = int(F[i])
    if N == 0:
        print "INSOMNIA"
        o.write("INSOMNIA")
    else: 
        while True:
            for c in str(N):
                test = test.replace(c, '')
            if test == "":
                print N
                o.write(str(N))
                break
            else:
                N = N + int(F[i])
    o.write("\n")
o.close()
    
    
