
import sys
from time import time
#from math import *
#import itertools

def init_script(infilecode, is_practice = False):
    global start_time, fin, fout, printoutput
    start_time = time()
    practice_filename_options = {'E':'example.txt','A1':'A-small-practice.in','A2':'A-large-practice.in','B1':'B-small-practice.in','B2':'B-large-practice.in','C1':'C-small-practice.in','C2':'C-large-practice.in','D1':'D-small-practice.in','D2':'D-large-practice.in'}
    filename_options = {'E':'example.txt','A1':'A-small-attempt0.in','A2':'A-large.in','B1':'B-small-attempt1.in','B2':'B-large.in','C1':'C-small-attempt1.in','C2':'C-large.in','D1':'D-small-attempt1.in','D2':'D-large.in'}
    file_in = practice_filename_options[infilecode] if is_practice else filename_options[infilecode]
    fin = open(file_in, 'r')
    sys.stdin = fin
    foutname = fin.name.replace(".in",".out.txt") if file_in != 'example.txt' else 'example.out.txt'
    fout = open(foutname, 'w')
    printoutput = lambda *args: print(*args, flush = True, file = fout) or print(*args, flush = True, file = sys.stdout)

def end_script():
    print("Elapsed time =", round(time()-start_time,3), "seconds.")    



init_script('A2', is_practice = False)

T = int(input())  #number of cases

for case in range(1,T+1):

    ans = 0
    N, R, P, S = [int(x) for x in input().split()]
    
    if abs(R-P) > 1 or abs(R-S) > 1 or abs(S-P) > 1:
       printoutput("Case #"+str(case)+":", 'IMPOSSIBLE')
       continue

    #G = ['P':'PR','S':'PS','R':'RS']

    F = [0]*(N+1)

    F[0] = ('P','S','R')
    n = 0
    f = ('PR','PS','RS')
    n = 1

    while n<N:
        #for f in F:
            fa = f[0]
            fb = f[1]
            fc = f[2]
            ga = min(fa+fb,fb+fa)
            gb = min(fa+fc,fc+fa)
            gc = min(fc+fb,fb+fc)
            f=(ga,gb,gc)
            n+=1

    for opt in f:
        if P == opt.count('P') and R == opt.count('R'):
            ans = opt
      
               
    printoutput("Case #"+str(case)+":", ans)
    
    

end_script()