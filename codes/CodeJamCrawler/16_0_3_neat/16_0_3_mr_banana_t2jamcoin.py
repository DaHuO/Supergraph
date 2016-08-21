from math import sqrt
def interpret(x,base):
    result=0
    for i in range(len(str(x))):
        result+=int(str(x)[len(str(x))-i-1])*(base**i)
    return result
def ffactor(x):
    for i in range(2,int(sqrt(x))+1):
        if not x%i:
            return i
        if i>=10000000:
            return 0
    else:
        return 0
t=int(input())
for case in range(1,t+1):
    li=[int(i) for i in input().split()]
    n=li[0]
    l1=[]
    print('Case #%s:'%case)
    for i in range(2**(n-2),2**(n-1)):
        l2=[]
        for j in range(2,11):
            l2.append(ffactor(interpret(bin(i)[2:]+'1',j)))
            if not l2[-1]:
                break
        else:
            l1.append([bin(i)[2:]+'1']+[str(i) for i in l2])
            print(' '.join(l1[-1]))
            if len(l1)>=li[1]:
                break
        
