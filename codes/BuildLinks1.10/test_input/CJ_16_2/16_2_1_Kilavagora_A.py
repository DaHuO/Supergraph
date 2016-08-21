#!/usr/bin/python3
import fileinput
f=fileinput.input()
T=int(f.readline())

repr_chr="ZWUXGOHFSN"
repr_num={
 "Z":"0",
 "W":"2",
 "U":"4",
 "X":"6",
 "G":"8",
 "O":"1",
 "H":"3",
 "F":"5",
 "S":"7",
 "N":"9"   
    }
repr_map={
 "Z":"ZERO",
 "W":"TWO",
 "U":"FOUR",
 "X":"SIX",
 "G":"EIGHT",
 "O":"ONE",
 "H":"THREE",
 "F":"FIVE",
 "S":"SEVEN",
 "N":"NINE"
    }

    
for case in range(T):
    wdict={}
    out=[]
    S=f.readline().strip()
    for c in S:
      wdict[c]=wdict.get(c,0)+1
      
    for c in repr_chr:
        while (c in wdict):
            out.append(repr_num[c])
            for r in repr_map[c]:
                if wdict[r]>1:
                    wdict[r]-=1
                else: 
                    wdict.pop(r,None)
                    
    print("Case #"+str(case+1)+":",''.join(sorted(out)))
    
