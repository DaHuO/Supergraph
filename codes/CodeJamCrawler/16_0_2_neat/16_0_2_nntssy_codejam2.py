def flipAllPancakes(line):
    if not('-' in line) or len(line)==0:
        return 0
    elif line[-1]=='-':
        newLine=''
        for cake in line:
            if cake=='+':
                newLine+='-'
            else:
                newLine+='+'
        return 1+flipAllPancakes(newLine)
    else:
        return flipAllPancakes(line[:-1])    
           
def main(fin,fout):
    numCases=int(fin.readline())
    for i in range(numCases):
        case=fin.readline()
        fout.write('Case #'+str(i+1)+': '+str(flipAllPancakes(case))+'\n')
        
fin=open('C:\Users\exin1\Google Drive\Study\Google CodeJam\B.in','r')
fout=open('C:\Users\exin1\Google Drive\Study\Google CodeJam\B.out','w')
main(fin,fout)
fin.close()
fout.close()