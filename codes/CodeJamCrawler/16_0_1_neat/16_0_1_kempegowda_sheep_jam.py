from math import *
arr=[0,1,2,3,4,5,6,7,8,9]
def remove(n):
    rem=0
    while(n!=0):
        rem=n%10
        try:
            arr.remove(rem)
        except:
            pass
        n=n/10
        
        
t=int(raw_input())
for i in range(1,t+1):
    n=int(raw_input())
    if n==0:
        print "Case #"+`i`+": INSOMNIA"
    else:
        remove(n)
        j=1
        while(len(arr)!=0):
            remove(n*j)
            j=j+1
        print "Case #"+`i`+": "+`n*(j-1)`
    arr=[0,1,2,3,4,5,6,7,8,9]
