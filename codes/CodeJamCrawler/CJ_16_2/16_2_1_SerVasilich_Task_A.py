fi=open("A-large.in"); fo=open("A-large.out","w")
#fi=open("A-small-attempt0.in"); fo=open("A-small-attempt0.out","w")

from collections import *

def fnd():
    d=Counter()
    a=[0]*10
    for k in fi.readline().strip(): d[k]+=1
    a[0]=d['Z']; d['Z']-=a[0]; d['E']-=a[0]; d['R']-=a[0]; d['O']-=a[0]
    a[2]=d['W']; d['T']-=a[2]; d['W']-=a[2]; d['O']-=a[2]
    a[6]=d['X']; d['S']-=a[6]; d['I']-=a[6]; d['X']-=a[6]
    a[4]=d['U']; d['F']-=a[4]; d['O']-=a[4]; d['U']-=a[4]; d['R']-=a[4]
    a[3]=d['R']; d['T']-=a[3]; d['H']-=a[3]; d['R']-=a[3]; d['E']-=a[3]*2
    a[8]=d['G']; d['E']-=a[8]; d['I']-=a[8]; d['G']-=a[8]; d['H']-=a[8]; d['T']-=a[8]
    a[5]=d['F']; d['F']-=a[5]; d['I']-=a[5]; d['V']-=a[5]; d['E']-=a[5]
    a[7]=d['V']; d['S']-=a[7]; d['E']-=a[7]*2; d['V']-=a[7]; d['N']-=a[7]
    a[1]=d['O']; d['O']-=a[1]; d['N']-=a[1]; d['E']-=a[1]
    a[9]=d['E']
    return ''.join([str(i)*a[i] for i in range(10)])        

for T in range(int(fi.readline())):     
    print("Case #"+str(T+1)+":",fnd(),file=fo)
    
fi.close()
fo.close()
print("OK")