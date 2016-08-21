def flip_pancaces(pancaces,good='+'):
    if pancaces==good*len(pancaces):
        return 0 
    elif pancaces[-1]==good:
        return flip_pancaces(pancaces[:-1],good)
    else:
        if good=='+':
            new_good='-'
        elif good=='-':
            new_good='+'
        return 1+flip_pancaces(pancaces[:-1],new_good)
        
def solve_problemB(fname):
    fin=open(fname)
    flines=fin.readlines()
    fin.close()
    fout=open(fname.split('.')[0]+'.out','w')
    for i in range(1,len(flines)):
        pancaces=flines[i].split()[0]
        flips=flip_pancaces(pancaces)
        fout.write('Case #'+str(i)+': '+str(flips)+'\n')
    fout.close()
        
        
        