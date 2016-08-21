import numpy
import sys
import string

lst = [['Z','ZERO'],
       ['W','TWO'],
       ['U','FOUR'],
       ['X','SIX'],
       ['G','EIGHT'],
       ['O', 'ONE'],
       ['T','THREE'],
       ['F','FIVE'],
       ['V','SEVEN']
]

od = [0,2,4,6,8,1,3,5,7]
def solve(d):
    arr = [0 for cnt in range(10)]
    for e in range(9):
        #print d
        if d.has_key(lst[e][0]) and d[lst[e][0]]>0:
            cnt = d[lst[e][0]]
            arr[od[e]] = cnt
            for c in lst[e][1]:
                d[c]=d[c]-cnt
    try:
        arr[9]=d['I']
    except:
        pass
    ans=[]
    for e,ele in enumerate(arr):
        cpy = ele
        while cpy>0:
            cpy=cpy-1
            ans.append(str(e))
    return ans

f=open(sys.argv[1])
f.readline()
for e,ln in enumerate(f):
    d=dict()
    for c in ln:
        try:
            d[c]=d[c]+1
        except:
            d[c]=1
    print "Case #"+str(e+1)+': '+''.join(solve(d))
    
