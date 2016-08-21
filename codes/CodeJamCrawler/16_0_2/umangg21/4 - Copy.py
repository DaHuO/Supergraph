
t=int(input())

def find(b,count):
    past=''
    now=b[0]
    for i in b:
        if i=='-' and i==past:
            past=i        
        elif i=='-' and past=='':
            past=i
            count=1
        elif i=='-' and past=='+':
            past=i
            count+=2
        elif i=='+' and i!= past:
            past=i
        elif i=='+' and i==past:
            past=i
    return count
        
  
for k in range(t):

    n=input()
    count=(len(n))
    minus=n.count('-')
    plus=n.count('+')

    if(plus==count):
        print("Case #{}: 0".format(k+1))
    elif(minus==count):
        print("Case #{}: 1".format(k+1))
    else:
        count=0
        c=list(n)
        count=find(c,count);
        print("Case #{}: {}".format(k+1,count))

    




   
