ipname = input("Enter the name of input file : ")
ip = open(ipname, "r")
o1 = "Output "
extension = ".txt"
outputname = o1 + ipname[:-3] + extension
out = open(outputname, "w")

t = ip.readline();t=int(t)

for t_i in range(t):
    pc = ip.readline(); pc = list(pc);
    if(t_i!=t-1):
        pc = pc[:-1]
    count = 0
    lenth = len(pc)
    if lenth == 1 and pc[0]=='-':
        count=1
    elif lenth==1 and pc[0]=='+':
        count=0
    if(lenth>=2):
        for i in range(len(pc)-1):
            if(pc[i]!=pc[i+1]):
                count += 1
        if(pc[-1]=='-'):
            count += 1
    out.writelines("Case #%d: %d\n" % (t_i+1,count))

ip.close()
out.close()
