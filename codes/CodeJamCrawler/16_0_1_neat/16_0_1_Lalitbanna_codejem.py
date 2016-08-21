def fun(N):
    s=str(N)
    dic=[]
    for x in s:
        if x not in dic:
           dic.append(x)
    return dic


def sleep(N):
    if N==0:
        return "INSOMNIA"
    i=0
    dic=[]
    DIC=['0','1','2','3','4','5','6','7','8','9']
    while dic!=DIC:
        i += 1
        x=fun(N*i)
        for y in x:
                if y not in dic:
                    dic.append(y)
                    dic.sort()
    return N*i

N = raw_input()
for x in range(int(N)):
    num = raw_input()
    print "Case #"+str(x+1)+": " + str(sleep(int(num)))

