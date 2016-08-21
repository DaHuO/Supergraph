from sys import stdin as ip
f=open('op.txt',"w")
for _ in xrange(int(ip.readline())):
    k,c,s=map(int,ip.readline().split())
    f.write("Case #%d: "%(_+1))
    for i in xrange(1,k+1):
        f.write(str(i)+" ")
    f.write("\n")
f.close()
