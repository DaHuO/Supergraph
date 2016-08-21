from math import factorial as fff
from fractions import gcd
from itertools import combinations as c
f=pow(2,3,3)
xs=fff(f+2)
author='biggy_bs'
# Main code goes here !!
dp=[0]*110
val_dic={}
t=input()
case=1
while t>0:
    t-=1
    l=[]
    st=''
    k,c,s=map(int,raw_input().split())
    print 'Case #'+str(case)+':',
    for i in range(1,k+1):
        print i,
    print ''    
    case+=1
