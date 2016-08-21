input = open("files.txt","r")
output = open("output.txt","w")

T = input.readline()
T = int(T)
for i in range(T):
    ns = input.readline()
    n = int(ns)
    if n == 0:
        output.write("Case #{0}: INSOMNIA\n".format(i+1))
    else:
        bool = False
        tabV = list()
        k=0
        inter=n
        while not bool and len(tabV)<10:
            k+=1
            inter=k*n
            ns=str(inter)
            for nb in ns:
                if nb not in tabV:
                    tabV.append(nb)            
        output.write("Case #{0}: {1}\n".format(i+1,ns))