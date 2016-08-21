f = open('Revenge of the Pancakes.txt', 'w')
T = int(raw_input())
for j in range(T):
    S=raw_input()
    S=S[::-1]
    a='i'
    for i in S:
        if a=='i':
            if i=='+':
                n=0
                a='+'
            else:
                n=1
                a='-'
        elif a=='+':
            if i=='-':
                n+=1
                a='-'
        elif a=='-':
            if i=='+':
                n+=1
                a='+'
    f.write("Case #"+str(j+1)+": "+str(n)+"\n")
    
    
