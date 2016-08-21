import itertools
from timeit import timeit

def generate(n):
    i=range(n)
    s=list(itertools.combinations(i,2))
    l=[]
    for i in s:
        if (abs(i[0]-i[1]))%2==1:
            l.append(i)
    ans=[]
    for i in l:
        ans.append('0'*i[0]+'1'+'0'*(abs(i[0]-i[1])-1)+'1'+(n-i[1]-1)*'0')

    final=[]
    for i in ans:
        final.append('1'+i+'1')
    #return len(final)
    ff=[]
    for i in final:
        l=[]
        for j in range(len(i)):
            if i[j]=='0':
                l.append(j)
        
        s=list(itertools.combinations(l,2))
        ll=[]
        for k in s:
            if (abs(k[0]-k[1]))%2==1:
                ll.append(k)
        for m in ll:
            ff.append(i[:m[0]]+'1'+i[m[0]+1:m[1]]+'1'+i[m[1]+1:])
    #print ff
    yoooo=ff+final
    lll=[]
    for i in yoooo:
        if len(lll)<500:
            if i not in lll:
                lll.append(i)
            

    return map(int, lll)
    #for i in range(50):
     #   answer.append(int(yoooo[i]))
    #answer has 50 values    
s = set()
def test(i):
    for r in range(2,11):
        if int(str(i),r)%(r+1):
            print "###ERR"
    if i in s:
        print "###ERR", i
    else:
        s.add(i)

t=int(raw_input())
for i in range(t):
    print "Case #{}:".format(i+1)
    n,j = map(int, raw_input().strip().split())
    c = 0
    for i in generate(n-2):
        test(i)
        print "{} 3 4 5 6 7 8 9 10 11".format(i)
        c += 1


    
    '''s1=list(itertools.combinations(i,4))
    l=[]
    for i in s1:
        s=list(itertools.combinations(i,2))
        
        
#timeit('generate(14)', setup='from __main__ import generate', number=1000)'''
