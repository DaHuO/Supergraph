'''
Created on Mar 19, 2016

@author: elmoatasem
'''




def solve_problem(N):
    res = 0
    h = {}
    solved = False
    NString = str(N)
    oldNString = ""
    itr = 1
    M = N
    while(True):
        Nlist = list(NString)
        if(NString == oldNString and len(h.keys()) <> 10):
            break
        else:
            for i in range(len(Nlist)):
                if(h.get(Nlist[i]) == None):
                    h[Nlist[i]] = 1
            if(len(h.keys()) == 10):
                solved = True
                break
            else:
                oldNString = NString
                itr = itr + 1
                N = itr*M;
                NString = str(N)
                
    if(solved):
        res =  N
    else: 
        res = 'INSOMNIA' 
                    
    return res





f_r = open('A-large.in',"r")
n_test=int(f_r.readline().strip()) 
f_w = open("A.out", "w")
result = ""
for i in range(n_test):
    N = int(f_r.readline().strip())
    result = solve_problem(N)
    print result
    output_str='Case #{itr}: {res}'.format(itr=(i+1),res=result)
    f_w.write(output_str+'\n')
    
f_r.close()


