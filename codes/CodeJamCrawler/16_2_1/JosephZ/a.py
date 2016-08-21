filename="A-small-attempt1.in"
f1=open(filename)
number=int(f1.readline())
result_list=list()
import collections

d1={0:["Z","E","R","O"],
    1:["O","N","E"],
    2:["T","W","O"],
    3:["T","H","R","E","E"],
    4:["F","O","U","R"],
    5:["F","I","V","E"],
    6:["S","I","X"],
    7:["S","E","V","E","N"],
    8:["E","I","G","H","T"],
    9:["N","I","N","E"]}

def check(d,n):
    for i in d1[n]:
        if i not in d.keys():
            return False
        if d[i]==0:
            return False
        if (n==3) and (d["E"]<2):
            return False
        if (n==7) and (d["E"]<2):
            return False
        if (n==9) and (d["N"]<2):
            return False
    return True

def dfs(d,n):
    if n==10:
        for i in d.keys():
            if d[i]!=0:
                return "X"
        return " "
    if check(d,n):
        newd=d.copy()
        for i in d1[n]:
            newd[i]=newd[i]-1
        #print(newd,n)
        result=dfs(newd,n)
        if result[-1]!="X":
            return str(n)+result
    return dfs(d,n+1)

def work(input_string):
    d2=dict(collections.Counter(input_string))
    return dfs(d2,0)

for i in range(number):
    info=f1.readline().strip()
    t=work(info)
    result_list.append(t) 
    


f2=open("output.txt",'w+')
for i in range(len(result_list)):
        line="Case #"+str(i+1)+": "+str(result_list[i])+'\n'
        f2.write(line)
f2.close()
