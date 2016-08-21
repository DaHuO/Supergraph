def create_all_mono(k):
    monos=[]
    for i in range(k):
        mono=['L']*k
        mono[i]='G'
        monos.append(''.join(mono))
    return monos
    
def create_complexity(k,c):
    monos=create_all_mono(k)
    complexes=monos[::]
    for i in range(1,c):
        new_complexes=[]
        for j in range(k):
            new_complex=''
            for tile in complexes[j]:
                if tile=='G':
                    new_complex+='G'*k
                else:
                    new_complex+=monos[j]
            new_complexes.append(new_complex)
        complexes=new_complexes[::]
    for compl in complexes:
        print compl
    max_gs=0
    for i in range(len(complexes[0])):
        gs=0
        for compl in complexes:
            if compl[i]=='G':
                gs+=1
        if gs>max_gs:
            max_gs=gs
    print max_gs
    
def solve_small(fname):
    fin=open(fname)
    flines=fin.readlines()
    fin.close()
    fout=open(fname.split('.')[0]+'.out','w')
    for i in range(1,len(flines)):
        k,c,s=flines[i].split()
        answers=range(1,int(k)+1)
        fout.write('Case #'+str(i)+': ')
        for answer in answers:
            fout.write(' '+str(answer))
        fout.write('\n')
    fout.close()
    
    
            
                
    