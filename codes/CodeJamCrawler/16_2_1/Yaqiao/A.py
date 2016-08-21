def FindNum(string):
    D={}
    D[0]="ZERO"
    D[1]="ONE"
    D[2]="TWO"
    D[3]="THREE"
    D[4]="FOUR"
    D[5]="FIVE"
    D[6]="SIX"
    D[7]="SEVEN"
    D[8]="EIGHT"
    D[9]="NINE"
    ans=[]
    def backtrack(string,ls):
        if len(string)==0:
            ans.append(ls)
            return
        for i in range(10):
            flag=1
            for j in D[i]:
                if j not in string:
                    flag=0
                    break
            if flag:
                remain=substract(string,D[i])
                backtrack(remain,ls+[i])
        
    backtrack(string,[])
    return ans[0]
                
def substract(string,seg):
    res=""
    for i in string:
        if i not in seg:
            res+=i
        else:
            tmp=list(seg)
            p = seg.index(i)  # find position of the letter "a"
            del(tmp[p])
            seg="".join(tmp)
                        
                        
    return res                


if __name__=="__main__":
    ls=[]
    with open('A-small.in','r') as r:
        for lines in r:
            ls.append(lines.strip())
    f=open('A_result.txt','w')
    nums=int(ls[0])
    for i in range(nums):
        array=FindNum(string)
        result=''.join(str(x) for x in array)
        f.write('Case #%d: '%(i+1)+result+'\n')
    f.close()    
