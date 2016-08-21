for t in range(int(input())):
    n=int(input())
    op=[]
    dig=['0','1','2','3','4','5','6','7','8','9']
    m=n
    if n==0:
        print('Case #',end='')
        print(t+1, end='')
        print(': ',end='')
        print('INSOMNIA')
    else:
        while op!=dig:
            for i in str(m):
                if i not in op:
                    op.append(i)
                    op=sorted(op)
                    #print(op)
            m+=n
        print('Case #',end='')
        print(t+1, end='')
        print(': ',end='')
        print(m-n)
        
