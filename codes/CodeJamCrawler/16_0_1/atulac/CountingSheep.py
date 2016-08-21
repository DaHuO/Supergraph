from collections import defaultdict
inp=open('A-large.in')
out=open('output.txt','w')
for test_case in range(int(inp.readline().strip())):
    occurence=defaultdict(int)
    n=int(inp.readline())
    if n==0:
        out.write("Case #"+str(test_case+1)+": "+"INSOMNIA\n")
    else:
        num=n
        count=0
        while count!=10:
            s=str(n)
            for each in s:
                if occurence[each]==0:
                    occurence[each]=1
                    count+=1
            n+=num
        out.write("Case #"+str(test_case+1)+": "+str(n-num)+"\n")
                
                
