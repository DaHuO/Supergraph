
def getvalue(line):
    res = line.split(' ')
    for i in range(len(res)):
        res[i] = int(res[i])
    return res
    

def parse(path):
    files = open(path)
    files.readline()
    content = files.readlines()
    for i in range(len(content)):
        content[i] = getvalue(content[i])
    return content
    

def notin(L,n):
    for i in range(len(L)):
        if L[i] == n:
            return False
    return True

def remove(L,n):
    res = []
    for i in range(len(L)):
        if L[i] != n:
            res.append(L[i])
    return res

def missing(papers, index):
    n = papers[index][0]
    L = []
    for i in range(1,n*2):
        for j in range(n):
            if(notin(L,papers[index+i][j])):
                L.append(papers[index+i][j])
            else:
                L = remove(L,papers[index+i][j])
    return sort(L,0,len(L)-1)

def merge(L1,L2):
    res = []
    l1 = len(L1)
    l2 = len(L2)
    i = 0
    j = 0
    while(i<l1 and j<l2):
        if L1[i] < L2[j]:
            res.append(L1[i])
            i += 1
        else:
            res.append(L2[j])
            j += 1
    while i<l1:
            res.append(L1[i])
            i += 1
    while j<l2:
            res.append(L2[j])
            j += 1
    return res

            

def sort(L,start,end):
    if(start == end):
        return [L[end]]
    else:
        m=(start+end)//2
        return merge(sort(L,start,m),sort(L,m+1,end))


def buildstring(missing):
    res = ""
    for i in range(len(missing)):
        res = res+str(missing[i])+" "
    return res

def output():
    data=(parse("B-large.in"))
    L = []
    i = 0
    n=1
    while(i<len(data)):
        L.append("Case #"+str(n)+": "+buildstring(missing(data,i))+"\n")
        n += 1
        i += 2*data[i][0]
    output=(open("outputrank.out","w"))
    output.writelines(L)

output()