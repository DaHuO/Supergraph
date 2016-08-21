import sys
def f(path):
    with open(path) as fil:
             lis=fil.readlines()
    out= open("out.txt","a")
    i=0
    for j in range(int(lis[0])):
        i+=1
        lst= range(1, int(lis[j+1].split()[0]) +1)
        out.write("Case #%d:" %i)
        for n in lst:
            out.write(" %d"%n)
        if j!=int(lis[0])-1:
            out.write("\n")
    out.close()

f(sys.argv[1])
