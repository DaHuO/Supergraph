def seeAllNumbers(N):
    if N==0:
        return 'INSOMNIA'
    else:
        seenNumbers=''
        digits='0123456789'
        i=1
        while len(digits)!=0:
            seenNumbers+=str(i*N)
            for digit in seenNumbers:
                n=digits.find(digit)
                if n==-1:
                    pass
                elif n==0:
                    digits=digits[1:]
                elif n==len(digits)-1:
                    digits=digits[:-1]
                else:
                    digits=digits[:n]+digits[n+1:]
            i+=1
        return str((i-1)*N)               

def main(fin,fout):
    numCases=int(fin.readline())
    for i in range(numCases):
        case=int(fin.readline())
        fout.write('Case #'+str(i+1)+': '+seeAllNumbers(case)+'\n')
        
fin=open('C:\Users\exin1\Google Drive\Study\Google CodeJam\codejam1.in','r')
fout=open('C:\Users\exin1\Google Drive\Study\Google CodeJam\codejam1.out','w')
main(fin,fout)
fin.close()
fout.close()