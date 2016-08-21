

def parse(path):
    files = open(path)
    files.readline()
    content = files.readlines()
    for i in range(len(content)):
        content[i] = content[i][:-1]
    return content
    
def countLetters(word):
    L = []
    for i in range(26):
        L.append(0)
    for i in range(len(word)):
        L[ord(word[i])-ord('A')] += 1
    return L

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
    if(start >= end):
        return [L[end]]
    else:
        m=(start+end)//2
        return merge(sort(L,start,m),sort(L,m+1,end))


def getNumber(word):
    L = countLetters(word)
    res = []
    for i in range(L[6]):#G 8
        res.append(8)
        L[19]-=1
        L[8]-=1
    for i in range(L[25]):#Z 0
        res.append(0)
        L[14]-=1
    for i in range(L[22]):#W 2
        res.append(2)
        L[19]-=1
        L[14]-=1
    for i in range(L[23]):#X 6
        res.append(6)
        L[18]-=1
        L[8]-=1
    for i in range(L[18]):#S 7
        res.append(7)
        L[21]-=1
        L[13]-=1
    for i in range(L[21]):#V 5
        res.append(5)
        L[5]-=1
        L[8]-=1
    for i in range(L[5]):#F 4
        res.append(4)
        L[14]-=1
    for i in range(L[19]):#T 3
        res.append(3)
    for i in range(L[14]):#O 1
        res.append(1)
    for i in range(L[8]):#I 9
        res.append(9)
    return sort(res,0,len(res)-1)


def getString(L):
    res = ""
    for i in range(len(L)):
        res += str(L[i])
    return res


def output():
    data=(parse("A-large.in"))
    L = []
    for n in range(len(data)):
        L.append("Case #"+str(n+1)+": "+getString(getNumber(data[n]))+"\n")
    output=(open("outputPhone.out","w"))
    output.writelines(L)

output()
