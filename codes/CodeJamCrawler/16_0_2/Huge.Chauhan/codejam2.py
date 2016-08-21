def change(s):
    s=s.replace('-','*')
    s=s.replace('+','-')
    s=s.replace('*','+')
    return s
z=int(input())
for i in range(1,z+1):
    x=input()
    num=0
    empty=''
    if empty=='-'*len(x):
        print("Case #{}: {}".format(i,1))
    elif empty=='+'*len(x):
        print("Case #{}: {}".format(i,0))
    else:      
        while len(x)>0:
            if x[-1]=='+':                
                x=x[:-1]                   
            else:
                x=change(x)
                num+=1
        print("Case #{}: {}".format(i,num))
