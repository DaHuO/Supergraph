#4
#2
#2 2
from __future__ import division
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#if the second of remaining would be <50.00001
#take 1
#else


def getSum(tuple):
     count = 0
     for a in tuple: count+=a[1]
     return count
    
def calculate(tuple):
    stringa = ""
    tuple = sorted(tuple,key=lambda x:x[1], reverse=True)
    
    while(1):
        next_max = tuple[1][1]
        if next_max/(getSum(tuple)-1) > 0.5:
            stringa = stringa+' '+tuple[0][0]+tuple[1][0]
            tupleA= [(tuple[0][0],int(tuple[0][1]-1)),(tuple[1][0],int(tuple[1][1]-1))]
            tupleA.extend(tuple[2:])
            tuple = tupleA
        else:
            stringa = stringa+' '+tuple[0][0]
            tupleA= [(tuple[0][0],int(tuple[0][1]-1))]
            tupleA.extend(tuple[1:])
            tuple = tupleA
        tuple = sorted(tuple,key=lambda x:x[1], reverse=True)
        if tuple[0][1]==0:return stringa



file = open('FS_A_small1.in','r')
total = int(file.readline())
for i in range(1,total+1):

    N_parties = int(file.readline())
    Seq = file.readline()
    
    Tuple_parties = []
    
    for p in range(N_parties): 
        Tuple_parties.append((ALPHA[p],int(Seq.split()[p])))
     
    str_solution = calculate(Tuple_parties)


    print 'case #%d: %s' % (i,str_solution)
       
    
