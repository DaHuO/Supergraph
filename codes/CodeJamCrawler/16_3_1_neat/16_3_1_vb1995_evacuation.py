
names = [ chr(x) for x in range(65,65+26) ]

def check(p,total):
    total = total/2.0
    for i in p:
        if i>total:
            return False
    return True

def getres(n,p):
    total = sum(p)
    res = ''
    
    while total!=0:
        remove = []
        
        for i in range(len(p)):
            if p[i]>0:
                p[i] = p[i] -1
                total = total -1
                if not check(p,total):
                    p[i] = p[i] + 1
                    total = total + 1
                else:
                    res = res + names[i] + ' '
                    remove.append(i)

        if not remove:
            remove = []
            for i in range(len(p)):
                if len(remove)==2:break
                for j in range(len(p)):
                    p[i] = p[i] -1
                    p[j] = p[j] -1
                    total = total - 2
                    if not check(p,total):
                        p[i] = p[i] + 1
                        p[j] = p[j] + 1
                        total = total + 2
                    else:
                        res = res + names[i] + names[j] + ' '
                        remove.append(i)
                        remove.append(j)
                        break
    return res

testcases = int(input())

for tc in range(1,testcases+1):
    n = int(input())
    p = [ int(x) for x in input().split() ] 
    print('Case #',tc,': ',getres(n,p),sep='')
