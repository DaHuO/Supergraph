def produceArt(seq,C):
    if C==1:
        return seq
    else:
        art=''
        for letter in seq:
            if letter=='L':
                art+=produceArt(seq,C-1)
            else:
                art+=produceArt(len(seq)*'G',C-1)
        return art        

def fractal(K,C,S):
    if C==1:
        if K==S:
            res=''
            for digit in range(1,K+1):
                res+=' '+str(digit)
            return res
        else:
            return 'IMPOSSIBLE'
    else:
        if K==1:
            return ' 1'
        else:
            res=''
            for digit in range(2,K+1):
                res+=' '+str(digit)
            return res             

def main(fin,fout):
    numCases=int(fin.readline())
    for i in range(numCases):
        case=fin.readline()
        case=case.split()
        fout.write('Case #'+str(i+1)+':'+fractal(int(case[0]),int(case[1]),int(case[2]))+'\n')
        
fin=open('C:\Users\exin1\Google Drive\Study\Google CodeJam\codejam4.in','r')
fout=open('C:\Users\exin1\Google Drive\Study\Google CodeJam\codejam4.out','w')
main(fin,fout)
fin.close()
fout.close()       