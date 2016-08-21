f = open("fractile.in",'r')
g = open("fractile_output.txt", 'w')
T = int(f.readline().strip())
for x in range(1,T+1):
    l = f.readline().strip().split()
    K = int(l[0])
    C = int(l[1])
    S = int(l[2])
    # just see first K tiles
    # if first letter is L, first K letters must be original seq
    # else all G
    r = range(1,K+1)
    for i in range(len(r)):
        r[i] = str(r[i])
    g.write("Case #" + str(x) + ": " + ' '.join(r) + '\n')
    
f.close()
g.close()
