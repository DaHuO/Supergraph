def getvalue(line):
    aux = line.split(' ')
    res = []
    for i in range(len(aux)):
        res.append(int(aux[i]))
    return res

def parse(path):
    files = open(path)
    files.readline()
    content = files.readlines()
    for i in range(len(content)):
        content[i] = getvalue(content[i])
    res = []
    for i in range(len(content)//2):
        res.append(content[2*i+1])
    return res
    

def maxL(L):
    m = 0
    im = 0
    im2 = False
    for i in range(len(L)):
        if (L[i] > m):
            m = L[i]
            im = i
            im2 = False
        if (L[i] == m):
            im2 = i
    return m,im,im2

def get1(L):
    pos = []
    for i in range(len(L)):
        if (L[i] == 1):
            pos.append(i)
    return pos

def evac(L):
    res = []
    m,im,im2 = maxL(L)
    while(m>2):
        m,im,im2 = maxL(L)
        if(not(im2)):
            res.append(str(chr(im+ord('A')))*2)
            L[im]-=2
            m-=2
        else:
            res.append(str(chr(im+ord('A')))+str(chr(im2+ord('A'))))
            L[im]-=1
            L[im2]-=1
            m-=1
    while(1):
        m,im,im2 = maxL(L)
        if (m==1):
            break
        res.append(str(chr(im+ord('A'))))
        L[im]-=1
        m,im,im2 = maxL(L)
        if (m==1):
            break
        res[len(res)-1]+=(str(chr(im+ord('A'))))
        L[im]-=1
    pos = get1(L)
    if(len(pos)%2):
        res.append(str(chr(pos.pop()+ord('A'))))
    while(len(pos)>0):
        res.append(str(chr(pos.pop()+ord('A')))+str(chr(pos.pop()+ord('A'))))
    return res
        

def getLine(L):
    res = L[0]
    for i in range(len(L)-1):
        res += " "+L[i+1]
    return res

def output():
    data=(parse("A-large.in"))
    L = []
    for n in range(len(data)):
        res = evac(data[n])
        L.append("Case #"+str(n+1)+": "+getLine(res)+"\n")
    output=(open("outputSenate.out","w"))
    output.writelines(L)

output()

    