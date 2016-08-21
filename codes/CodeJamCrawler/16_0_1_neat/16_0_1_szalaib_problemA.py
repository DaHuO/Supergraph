import pandas as pd
def get_sleep(N):
    if N==0:
        return 'INSOMNIA'
    n=N
    n_str=str(n)
    n_list=list(n_str)
    digits=set(n_list)
    while len(digits)<10:
        n=n+N
        n_str=str(n)
        n_list=list(n_str)
        digits=set(n_list)|digits
    return n
    
def write_sleep():
    fout=open('problemA_data.txt','w')
    fout.write('N,Last\n')
    for n in range(10**6+1):
        fout.write(str(n)+','+str(get_sleep(n))+'\n')
    fout.close()
    
def solve_problemA(fname):
    sleep_data=pd.read_table('problemA_data.txt',sep=',',header=0, index_col=[0])
    fin=open(fname)
    flines=fin.readlines()
    fin.close()
    fout=open(fname.split('.')[0]+'.out','w')
    for i in range(1,len(flines)):
        n=int(flines[i])
        l=sleep_data.loc[n,'Last']
        fout.write('Case #'+str(i)+': '+str(l)+'\n')
    fout.close()

    

    
        
    
    